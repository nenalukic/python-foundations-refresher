# Inspecting & Selecting Data with Pandas
# Exercise: Load a CSV file containing sales data with columns "month", "revenue", "expenses".


import pandas as pd

csv_data = """month,revenue,expenses
January,10000,7000
February,12000,8000
March,9000,6000
April,15000,9000
May,13000,8500
"""

# Create sales.csv
with open("sales.csv", "w", newline="") as f:
    f.write(csv_data)

# Load with pandas
df = pd.read_csv("sales.csv")

# Print requested outputs
#print(df.head())     # first 5 rows
#print(df.tail())     # last 5 rows
#print(df.shape)      # (rows, columns)
#print(df.columns)    # column names
#print(df.info())     # column types
#print(df.describe()) # summary statistics
#print(df["revenue"])        # Single column
print(df[["month", "revenue"]])  # Multiple columns
high_revenue = df[df["revenue"] > 6000]
print(high_revenue)

sorted_df = df.sort_values(by="revenue", ascending=False)
print(sorted_df)
