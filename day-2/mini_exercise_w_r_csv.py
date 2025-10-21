# 1. Create a CSV called sales.csv with columns: month, revenue.

# 2. Add 3–4 rows of fake data.

# 3. Write Python code to read and print each row in a nice format, e.g. 
# Output: 
# January: 10000
# February: 12000
# March: 9000

import csv
data = [
    ["January", 10000],
    ["February", 12000],
    ["March", 9000],
]

with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("✅ sales.csv created!")

with open("sales.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]}: {row[1]}")
