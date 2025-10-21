# Exercise: Create a file numbers.txt with numbers from 1 to 10 (each on a new line).
# Then read it and print:

# Create/write the file with numbers 1..10
with open("numbers.txt", "w") as file:
        for i in range(1, 11):
            file.write(f"{i}\n")

# Read the file and print each number formatted
with open("numbers.txt", "r") as file:
    for line in file:
        num = line.strip()
        if num:
            print(f"Number: {num}")
        