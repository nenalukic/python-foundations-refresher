# Reading Data from Files. Remeber that we've created two files: employees.csv and employee.json in day-2.
# Exercise: Read the data from both files into separate DataFrames and print them out.

import pandas as pd

df = pd.read_csv("employees.csv")
print(df.head())  # Shows first 5 rows

df = pd.read_json("employee.json")
print(df)
