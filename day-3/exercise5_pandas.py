# Using your sales DataFrame:

# Show only months with revenue > 6000.

# Sort by expenses in ascending order.

# Print only the month names of rows where revenue > expenses.

import pandas as pd

df = pd.read_csv("sales.csv")

high_revenue = df[df["revenue"] > 6000]
print("Months with revenue > 6000:")
print(high_revenue)

sorted_by_expenses = df.sort_values(by="expenses", ascending=True)
print("\nDataFrame sorted by expenses (ascending):")
print(sorted_by_expenses)

profit_months = df[df["revenue"] > df["expenses"]]["month"]
print("\nMonths where revenue > expenses:")
print(profit_months)