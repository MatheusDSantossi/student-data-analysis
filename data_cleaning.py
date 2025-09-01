import pandas as pd
import psycopg2
import os
from sqlalchemy import create_engine

from dotenv import load_dotenv

from utils.clean_data_functions import normalize_text, initials_from_name
from constants.states import brazilian_states
from utils.db_connection import get_connection
from utils.pandas_func import set_columns

load_dotenv()

# try:
    
#     conn = psycopg2.connect(
#         database="testqueries",
#         user="postgres",
#         password=os.getenv("POSTGRES_PASSWORD"),
#         host="localhost",  # e.g., 'localhost' or an IP address
#         port="5432"   
#     )
    
#     db_connection_str = f'postgresql+psycopg2://postgres:{os.getenv("POSTGRES_PASSWORD")}@localhost:5432/testqueries'
    
#     engine = create_engine(db_connection_str)
# except psycopg2.OperationalError as err:
#     print(f"Error conecting to the database: {err}")

conn, engine = get_connection()

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
result = cursor.fetchall()

# print("result: ", result)

df = pd.DataFrame(result)

# Close the connection
cursor.close()
conn.close()
print("-------------- ISNULL")
print(df.isnull().sum())
print("-------------- ISNA")
print(df.isna().sum())
# print("-------------- duplicates rows")
# print(df.duplicated())
print(df.info())


columns = ["campus", "unit", "course", "state", "city", "students_quantity"]

df = set_columns(columns, df)

# df["campus"] = df["campus"].str.replace(r"[^a-zA-Z0-9\s]", "", regex=True)

df["campus"] = df["campus"].apply(normalize_text)
df["unit"] = df["unit"].apply(normalize_text)
df["city"] = df["city"].apply(normalize_text)
df["state"] = df["state"].apply(normalize_text)

# Normalized mapping (so both keys and incoming values are compared normalized)
normalized_map = { normalize_text(k): v for k, v in brazilian_states.items() }

for v in brazilian_states.values():
    normalized_map[normalize_text(v)] = v

df_without_null = df.dropna(axis=0).copy()

states = df_without_null["state"].str.upper().str.strip()

uf = states.map(normalized_map)

# Applying fallback only wher mapping is NaN
fallback = states[uf.isna()].apply(initials_from_name)

# write fallback values into uf
uf = uf.fillna(fallback)

df_without_null["state"] = uf

# df_without_null["state"] = uf

print(df_without_null["state"])

# print("-------------- ISNULL")
# print(df_without_null.isnull().sum())
# print("-------------- ISNA")
# print(df_without_null.isna().sum())

# Inserting the DF data into an SQL table
table_name = "students_cleaned"

df_without_null.to_sql(
    name=table_name,
    con=engine,
    if_exists="append", # Options: 'fail', 'replace', 'append'
    index=False # If True the column index is write too
)

print(f"DataFrame successfully inserted into '{table_name} table.'")
