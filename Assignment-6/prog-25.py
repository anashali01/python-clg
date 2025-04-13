# Group words by their length using a dictionary.
words_list = list(input("Enter words separated by spaces: ").split())

dict_words_by_length = {}

for i in words_list:
    dict_words_by_length[i]=len(i)

print(dict_words_by_length)
