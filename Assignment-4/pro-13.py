def count_words(string):
    words = string.split()
    return len(words)

sentence = input("Enter a String: ")
counted_words = count_words(sentence)
print(f"{counted_words} words ") 