# Merging DataFrames using pandas

import pandas as pd

sales = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar"],
    "revenue": [5000, 7000, 6500]
})

costs = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar"],
    "expenses": [3000, 4000, 3500]
})

merged = pd.merge(sales, costs, on="month")
print(merged)
