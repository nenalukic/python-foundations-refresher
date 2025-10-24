# Load Cleaned CSV Data into SQLite Database
# After cleaning the API data in Day 4, the next step is to load that cleaned data into a SQLite database for further analysis.

import pandas as pd
import sqlite3
import glob
import os

# --- Step 1: Automatically find the latest cleaned CSV file ---
files = glob.glob("day-4/output/api_users_clean_*.csv")

print("🔍 Searching for cleaned CSV files in: day-4/output")
print("Found files:", files)

if not files:
    raise FileNotFoundError("No cleaned CSV files found in day-4/output/")

# Pick the most recent one based on creation time
csv_path = max(files, key=os.path.getctime)
print(f"📄 Using latest file: {csv_path}")

# --- Step 2: Load CSV into DataFrame ---
print("📂 Loading cleaned CSV data...")
df = pd.read_csv(csv_path)
print(f"✅ Loaded {len(df)} rows and {len(df.columns)} columns.")

# --- Step 3: Connect to SQLite database ---
db_path = "day-5/etl_data.db"
conn = sqlite3.connect(db_path)
print(f"Connected to SQLite database at: {db_path}")

# --- Step 4: Load data into a table ---
table_name = "api_users"
df.to_sql(table_name, conn, if_exists="replace", index=False)
print(f"💾 Data successfully written to table '{table_name}'.")

# --- Step 5: Verify data with SQL query ---
print("🔍 Running sample query...")
query = f"SELECT id, name, email, company_name FROM {table_name} LIMIT 5;"
sample = pd.read_sql_query(query, conn)
print(sample)

# --- Step 6: Close the connection ---
conn.close()
print("✅ Database connection closed.")

# Key Concepts:
# - Using glob to find files matching a pattern
# - Loading CSV data into pandas DataFrame
# - Connecting to SQLite with sqlite3
# - Writing DataFrame to SQL table with to_sql
# - Running SQL queries and reading results into DataFrame
# - Ensuring proper resource management by closing the database connection
