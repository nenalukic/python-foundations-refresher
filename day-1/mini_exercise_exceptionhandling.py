# Ask the user for a filename.
# Try to open it, if it doesn’t exist, print a nice message instead of crashing.

filename = input("Please enter a filename: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content successfully read.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")