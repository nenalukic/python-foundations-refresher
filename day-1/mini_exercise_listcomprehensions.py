# 1. From numbers 1–20, create a list of even numbers only.
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Even Numbers from 1 to 20:", even_numbers)

# 2. Create a list of word lengths for ["data", "python", "engineer"].

words = ["data", "python", "engineer"]
word_lengths = [len(word) for word in words]
print("Word Lengths:", word_lengths)