# Writing data to a file
with open("example.txt", "w") as file:
    file.write("Hello Data Engineer!\n")
    file.write("This is your Day 2 practice file.\n")

print("✅ File written successfully!")

# Reading the file
with open("example.txt", "r") as file:
    content = file.read()
   
print("File Content:")
print(content)

# Reading line by line
with open("example.txt", "r") as file:
    print("Reading line by line:")
    for line in file:
        print("Line:", line.strip())  # strip() removes extra newlines