import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils.pandas_func import set_columns

from utils.db_connection import get_connection

conn, engine = get_connection()

cursor = conn.cursor()

cursor.execute("SELECT * FROM students_cleaned")

result = cursor.fetchall()

df = pd.DataFrame(result)

columns = ["campus", "unit", "course", "state", "city", "students_quantity"]

df = set_columns(columns, df)

# print(df)

# Ensure numeric type for aggregation
df["students_quantity"] = pd.to_numeric(df["students_quantity"], errors="coerce").fillna(0)

# print(df["students_quantity"])

# Aggregate total students per state
students_by_state = df.groupby("state")["students_quantity"].sum()

# Optional: sort for readability
students_by_state = students_by_state.sort_values(ascending=False)

print("Aggregated totals by state:\n", students_by_state.head())
print(students_by_state.to_list())

# Plot bar chart using concrete arrays
# plt.figure(figsize=(12, 6))
# plt.bar(students_by_state.index.astype(str), students_by_state.values)
# plt.xlabel("State")
# plt.ylabel("Students (total)")
# plt.title("Total Students by State")
# plt.xticks(rotation=45, ha="right")
# plt.tight_layout()
# plt.show()

# print(df)

course_quantity_students = df.groupby("course")["students_quantity"].sum()

print(course_quantity_students.sort_values(ascending=False))

print("list: ", course_quantity_students.to_list())
print("values: ", course_quantity_students.values)

plt.plot()
plt.xlabel(course_quantity_students.index.astype(str).drop_duplicates())
plt.ylabel(course_quantity_students.values)
plt.show()

cursor.close()
conn.close()
