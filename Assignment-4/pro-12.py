#Sort Words in a sentence Alphabetically  
string = input("Enter a String: ")
words = string.split()
print(words)
word_sorted = sorted(words)
print(word_sorted)
string_sorted = " ".join(word_sorted)
print(string_sorted)
