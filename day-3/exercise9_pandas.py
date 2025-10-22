# Create two CSVs — revenue.csv and expenses.csv — both with a month column.
# Load them into Pandas and merge into a single dataset.
# Then calculate a new column profit = revenue - expenses.

import pandas as pd

# Create revenue DataFrame
revenue_data = {
    "month": ["Jan", "Feb", "Mar"],
    "revenue": [5000, 7000, 6500]
}
revenue_df = pd.DataFrame(revenue_data)

# Save to CSV
revenue_df.to_csv("revenue.csv", index=False)

# Create expenses DataFrame
expenses_data = {
    "month": ["Jan", "Feb", "Mar"],
    "expenses": [3000, 4000, 3500]
}
expenses_df = pd.DataFrame(expenses_data)

# Save to CSV
expenses_df.to_csv("expenses.csv", index=False)

# Load the CSVs
loaded_revenue = pd.read_csv("revenue.csv")
loaded_expenses = pd.read_csv("expenses.csv")

# Merge DataFrames on month
merged_df = pd.merge(loaded_revenue, loaded_expenses, on="month")

# Calculate profit column
merged_df["profit"] = merged_df["revenue"] - merged_df["expenses"]

# Print the final DataFrame
print(merged_df)

# Expected output:
#   month  revenue  expenses  profit
# 0   Jan     5000      3000    2000
# 1   Feb     7000      4000    3000
# 2   Mar     6500      3500    3000
