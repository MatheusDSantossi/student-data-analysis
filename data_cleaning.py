import pandas as pd
import psycopg2
import os
from sqlalchemy import create_engine

from dotenv import load_dotenv

from utils.clean_data_functions import _clean_campus

load_dotenv()

try:
    
    conn = psycopg2.connect(
        database="testqueries",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD"),
        host="localhost",  # e.g., 'localhost' or an IP address
        port="5432"   
    )
    
    db_connection_str = f'postgresql+psycopg2://postgres:{os.getenv("POSTGRES_PASSWORD")}@localhost:5432/testqueries'
    
    engine = create_engine(db_connection_str)
except psycopg2.OperationalError as err:
    print(f"Error conecting to the database: {err}")

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

df.columns = columns

# df["campus"] = df["campus"].str.replace(r"[^a-zA-Z0-9\s]", "", regex=True)

df["campus"] = df["campus"].apply(_clean_campus)
df["unit"] = df["unit"].apply(_clean_campus)
df["city"] = df["city"].apply(_clean_campus)

df_without_null = df.dropna()

print(df_without_null)

# Inserting the DF data into an SQL table
table_name = "students_cleaned"

df_without_null.to_sql(
    name=table_name,
    con=engine,
    if_exists="append", # Options: 'fail', 'replace', 'append'
    index=False # If True the column index is write too
)

print(f"DataFrame successfully inserted into '{table_name} table.'")
