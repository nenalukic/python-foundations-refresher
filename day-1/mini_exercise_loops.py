# Loop through numbers 1–10 and print:
# “Even” if divisible by 2
# “Odd” otherwise
# Hint: use % (modulo operator).

for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")