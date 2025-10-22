# Mini Project – Sales Data Analysis
# You have multiple CSV files in data/: sales_january.csv, sales_february.csv, sales_march.csv

# Each contains:
# day,revenue,expenses
# 1,200,150
# 2,220,140
# 3,180,160

# Your task:
# 1.Combine all files into one DataFrame.
# 2.Add a column month based on file name.
# 3.Compute total and average profit per month.
# 4.Save the cleaned dataset to cleaned_sales.csv.

import pandas as pd
from pathlib import Path

# Define base folder and data folder
base = Path.cwd() # current working directory
data_folder = base / "data" 
data_folder.mkdir(exist_ok=True)  # create folder if it doesn't exist

# Create sample data (only if missing)
sample = "day,revenue,expenses\n1,200,150\n2,220,140\n3,180,160\n"
for name in ("sales_january.csv", "sales_february.csv", "sales_march.csv"):
    p = data_folder / name
    if not p.exists():
        p.write_text(sample) 

# Find all sales CSV files in the data folder
files = sorted(data_folder.glob("sales_*.csv"))
if not files:
    print("No sales_*.csv files found in 'data/'.")
else:
    frames = []
    for f in files:
        df = pd.read_csv(f)
        month = f.stem.split("_")[-1].capitalize()
        df["month"] = month
        frames.append(df) 

    # Combine data
    combined = pd.concat(frames, ignore_index=True)
    combined["profit"] = combined["revenue"] - combined["expenses"]

    # Compute summary
    summary = (
        combined.groupby("month", sort=False)["profit"]
        .agg(total_profit="sum", avg_profit="mean")
        .reset_index()
    )

    # Save results (keep cleaned file in the same data folder)
    cleaned_path = data_folder / "cleaned_sales.csv"
    combined.to_csv(cleaned_path, index=False)

    # Print outputs
    print("Combined DataFrame:")
    print(combined)
    print("\nProfit summary per month:")
    print(summary)
