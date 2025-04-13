# 18. Remove all vowels from a string using a set.
vowels = {'a', 'e', 'i', 'o', 'u'}

def replace_vowels(string):
    for char in string:
        if char.lower() in vowels:
            string = string.replace(char, '*')
    return string

string = "Hello world"
print("String with vowels replaced:", replace_vowels(string))