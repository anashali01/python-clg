# Write a function that takes two strings and concatenates them with a space in between. If the
# second string is empty, return only the first string.
def concat_str (str1 , str2):
    if str2 == "":
        return str1
    else:
       return str1 + " " + str2
    

str1 = input("Enter First String :")
str2 = input("Enter Second String :")
print(concat_str(str1 , str2))