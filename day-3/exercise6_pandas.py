# Data Cleaning & Transformation with Pandas
# Handling Missing Values
import pandas as pd

data = {"name": ["Alice", "Bob", None], "age": [29, None, 25]}
df = pd.DataFrame(data)

print("Before cleaning:\n", df)

# Fill missing values
df["name"] = df["name"].fillna("Unknown")
df["age"] = df["age"].fillna(df["age"].mean())

print("\nAfter cleaning:\n", df)

# Transformations: changing column names & types

df.rename(columns={"age": "AgeYears"}, inplace=True)
df["AgeYears"] = df["AgeYears"].astype(int)
print("\nAfter transformation:\n", df)

# Apply a function to transform data: string operations
df["name"] = df["name"].str.upper()
print("\nAfter name transformation:\n", df)
