import json

employee = {
    "name": "Alice",
    "age": 29,
    "skills": ["Python", "SQL", "Airflow"]
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

print("✅ employee.json created!")

with open("employee.json", "r") as file:
    data = json.load(file)

print("Employee name:", data["name"])
print("Skills:", ", ".join(data["skills"]))
