par = """Hello world.
This is a python how  are you.
Python is great. """
print(par)
str = input("Enter Your word :")

sentence = par.split(".")
for sentence in sentence:
    if str in sentence:
        print(sentence)
  