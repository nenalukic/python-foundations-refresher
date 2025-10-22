# Exercise: Create a DataFrame with columns "name", "age", and "department".
# Populate it with at least 3 rows of sample data.
# Then print the DataFrame.

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [29, 34, 25],
    "department": ["Data Engineering", "Analytics", "Data Science"]
}

df = pd.DataFrame(data)
print(df)
