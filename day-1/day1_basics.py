# 1. Variables and Data Types

name = "Alice"        # String (text)
age = 30              # Integer
height = 1.68         # Float
is_engineer = True    # Boolean

# Example of printing variables
country = "Canada"
population = 38000000
area = 9.98  # in million kilometers

print(f"{country} has {population} people and covers {area} million km².")

# 2. Python Collections: Lists, Dictionaries, Tuples, and Sets

# LIST
numbers_list = [1, 2, 3, 4, 5]
numbers_list.append(6)
print("List:", numbers_list)

# DICTIONARY
person_dict = {"name": "Alice", "role": "Data Engineer"}
print("Dictionary:", person_dict["role"])

# TUPLE
coordinates_tuple = (10.0, 20.0)
print("Tuple:", coordinates_tuple[0])

# SET
unique_set = {1, 2, 3, 2, 1}
print("Set:", unique_set)

# 3. Loops & Conditionals 
# Loops let you repeat actions. Conditionals let you make decisions.

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
for city in cities:
    if "o" in city.lower():
        print(f"{city} contains the letter 'o'")
    else:
        print(f"{city} does not contain the letter 'o'")

# 4. Functions
# Functions are reusable pieces of code
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

# 5. List Comprehensions: a quick way to build lists.

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print("Squared Numbers:", squared_numbers)

# 6. Exception Handling (Error Management): when something goes wrong, you can catch and handle it.

try:
    value = int(input("Enter a number: "))
    print(10 / value)
except ValueError:
    print("That’s not a number!")
except ZeroDivisionError:
    print("You cannot divide by zero.")
finally:
    print("End of program.")

# 7. File Operations: reading from and writing to files.
with open("example.txt", "w") as file:
    file.write("Hello, World!")

with open("example.txt", "r") as file:
    print(file.read())