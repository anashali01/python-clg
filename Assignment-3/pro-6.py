# Count the occurrences of a specific character in a given string
str = "Hellllo"
find = input("Enter Char which you want to find:")
count = 0
i = 0
while i<len(str):
    if str[i] == find:
        count +=1
    i+=1

print("The Total Character of string",count)