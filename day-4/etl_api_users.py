# Reusable ETL pipeline: 
# Extract: fetch user data from an API (jsonplaceholder.typicode.com/users)
# Transform: clean and flatten nested JSON fields (address, company)
# Load: save the clean dataset as a timestamped CSV (so each run keeps a history)

import requests
import pandas as pd
import ast
from pandas import json_normalize
from datetime import datetime
import os

def extract_data(url):
    """Extract data from the API endpoint."""
    print("📡 Fetching data from API...")
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if request fails
    return response.json()


def safe_eval(text):
    """Safely evaluate string to dict if possible."""
    if pd.isna(text):
        return {}
    try:
        return ast.literal_eval(text)
    except Exception:
        return {}


def transform_data(data):
    """Flatten nested JSON and clean data."""
    print("🧹 Cleaning and transforming data...")
    df = pd.DataFrame(data)

    # Some APIs return nested objects; ensure consistent flattening
    if "address" in df.columns:
        df["address"] = df["address"].apply(lambda x: x if isinstance(x, dict) else safe_eval(str(x)))
        address_df = json_normalize(df["address"]).add_prefix("address_")
    else:
        address_df = pd.DataFrame()

    if "company" in df.columns:
        df["company"] = df["company"].apply(lambda x: x if isinstance(x, dict) else safe_eval(str(x)))
        company_df = json_normalize(df["company"]).add_prefix("company_")
    else:
        company_df = pd.DataFrame()

    clean_df = pd.concat([df.drop(["address", "company"], axis=1, errors="ignore"), address_df, company_df], axis=1)
    return clean_df


def load_data(df, output_dir="output"):
    """Save the cleaned data with a timestamp."""
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/api_users_clean_{timestamp}.csv"
    df.to_csv(filename, index=False)
    print(f"💾 Data saved to: {filename}")
    return filename


def main():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        raw_data = extract_data(url)
        clean_df = transform_data(raw_data)
        load_data(clean_df)
        print("✅ ETL pipeline completed successfully.")
    except Exception as e:
        print(f"❌ Pipeline failed: {e}")


if __name__ == "__main__":
    main()

# Key Takeaways:
# Modular ETL functions (Extract, Transform, Load) improve code clarity and reusability.
# Use requests to fetch API data and handle errors gracefully.
# Flatten nested JSON structures with pandas.json_normalize.
# Save output files with timestamps to maintain historical records.
