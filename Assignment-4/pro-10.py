# Write a function that checks whether two input strings are anagrams (contain the same 
# letters in a different order). 
def anagram(s1 , s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2
s1 = input("Enter First string :")
s2 = input("Enter Second string :")
s1.lower()
s2.lower()
print("True = anagram AND False = Not anagram")
print(anagram(s1 , s2))