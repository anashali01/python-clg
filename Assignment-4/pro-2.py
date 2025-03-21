# #Write a function that extracts and prints the first half and second half of a given string
# separately.
str = "hello world"
length = int(len(str)/2)
print(str[0:length])
print(str[length:])