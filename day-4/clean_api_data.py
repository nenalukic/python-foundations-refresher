# When you fetched data from https://jsonplaceholder.typicode.com/users, some columns (like address and company) were nested dictionaries.
# To clean this data for analysis, we need to flatten these nested structures into separate columns.

import pandas as pd
import ast
from pandas import json_normalize

def safe_eval(text):
    """Safely evaluate string to dict if possible."""
    if pd.isna(text):
        return {}
    try:
        return ast.literal_eval(text)
    except Exception:
        return {}

# Step 1: Load the messy CSV
df = pd.read_csv("api_users.csv")

# Step 2: Safely evaluate JSON-like columns
df["address"] = df["address"].apply(safe_eval)
df["company"] = df["company"].apply(safe_eval)

# Step 3: Flatten with prefixes to avoid collisions
address_df = json_normalize(df["address"]).add_prefix("address_")
company_df = json_normalize(df["company"]).add_prefix("company_")

# Step 4: Combine flattened columns with the main DataFrame
clean_df = pd.concat(
    [df.drop(["address", "company"], axis=1), address_df, company_df],
    axis=1
)

# Step 5: Save the clean version
clean_df.to_csv("api_users_clean.csv", index=False)

print("✅ Cleaned data saved to 'api_users_clean.csv'")
print(clean_df.head())

# Key Takeaways:
# Use ast.literal_eval() to Safely Parse “Fake JSON”
# Use pandas.json_normalize to flatten nested JSON structures.
# Prefixing Columns to Prevent Name Collisions
# Combining Cleaned DataFrames
# Always inspect your DataFrame after cleaning to ensure the structure is as expected.

