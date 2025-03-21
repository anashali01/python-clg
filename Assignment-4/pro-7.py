# Write a program that takes a sentence as input and generates its acronym.
# Example: "Machine Learning" → "ML"
str = input("Enter String :")
word = str.split()
accro = ''.join(i[0].upper() for i in str.split())
print(accro)