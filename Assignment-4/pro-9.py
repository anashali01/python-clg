# Write a function that replaces every occurrence of a banned word in a sentence with *****.
# Example: "Python is fun, but Java is difficult" (banned word: "Java") →
# "Python is fun, but ***** is difficult"
def bann(par , ban_word):
    return par.replace(ban_word , "*****")
par = "Hello coder hey anash"
ban_word = "coder"
print(bann(par , ban_word))