# Create a function that:
# Centers a string within 30 spaces (center()).Replaces vowels in a string with '*' (replace()).
def center_str (string):
    return string.center(30)

def vowel_str(string):
    vowel = "aeiouAEIOU"
    for i in vowel:
        string = string.replace(i , "*")
    return string
string = "Hello Nigga"
print(center_str(string))
print(vowel_str(string))