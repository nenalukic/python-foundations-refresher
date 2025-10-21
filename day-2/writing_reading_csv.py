import csv

data = [
    ["Name", "Age", "Department"],
    ["Alice", 29, "Data Engineering"],
    ["Bob", 34, "Analytics"],
    ["Charlie", 25, "Data Science"]
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("✅ employees.csv created!")

with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)