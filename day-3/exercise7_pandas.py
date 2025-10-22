# Aggregations and Grouping with Pandas


import pandas as pd

data = {
    "month": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar"],
    "region": ["East", "West", "East", "West", "East", "West"],
    "revenue": [200, 180, 220, 210, 250, 230]
}
df = pd.DataFrame(data)

grouped = df.groupby("month")["revenue"].sum()
print(grouped)
