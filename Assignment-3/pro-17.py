# Create a program that prints the multiplication table of a given number using a for
# loop.
num = int(input("Enter Number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
