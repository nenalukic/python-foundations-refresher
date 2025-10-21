# Create a JSON file config.json with this structure:
# {
#  "database": "postgres",
#  "user": "admin",
#  "password": "secret"
# }
# Then write Python code to read the file and print: Connecting to postgres as admin...

import json
config = {
    "database": "postgres",
    "user": "admin",
    "password": "secret"
}

with open("config.json", "w") as file:
    json.dump(config, file, indent=4)
print("✅ config.json created!")

with open("config.json", "r") as file:
    data = json.load(file)
print(f"Connecting to {data['database']} as {data['user']}...")
