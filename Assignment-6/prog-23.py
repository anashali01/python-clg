# 23. Count character frequency in a string using a dictionary.
char_dict = {}
string = input("Enter a string: ")

for char in string:
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1

print("Character frequency in the string:", char_dict)