# Create a Python program that stores a paragraph using triple quotes and extracts all 
# sentences that contain a specific word. ex(extract Python containing sentences ) 
par = """Hello world.
This is a python how  are you.
python is great. """
print(par)
str = input("Enter Your word :")

sentence = par.split(".")
for sentence in sentence:
    if str in sentence:
        print(sentence)
  