# You have 3 CSVs in a data/ folder:
# data/january.csv
# data/february.csv
# data/march.csv

# Each has:
# day,revenue
# 1,200
# 2,300
# 3,250

#Goal → Merge them into a single file all_months.csv.
import csv
from pathlib import Path

data_dir = Path("data")
output_file = data_dir / "all_months.csv"

# Create data directory and sample CSV files if they don't exist
data_dir.mkdir(exist_ok=True)
sample_data = {
    "january.csv": [("day", "revenue"), (1, 200), (2, 300), (3, 250)],
    "february.csv": [("day", "revenue"), (1, 220), (2, 330), (3, 270)],
    "march.csv": [("day", "revenue"), (1, 210), (2, 310), (3, 260)],
}

for filename, rows in sample_data.items():
    with open(data_dir / filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

# Merge CSV files
with open(output_file, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["day", "revenue"])  # Write header once

    for month in ["january.csv", "february.csv", "march.csv"]:
        with open(data_dir / month, "r", newline="") as infile:
            reader = csv.reader(infile)
            next(reader)  # Skip header
            for row in reader:
                writer.writerow(row)
print(f"Merged CSV files into {output_file}")

# Verify the merged file
with open(output_file, "r", newline="") as f:
    print(f.read())
