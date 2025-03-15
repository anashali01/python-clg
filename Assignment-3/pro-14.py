# Write a Python program to find the largest among three numbers using
# if...elif...else.
a = int(input("Enter First Number:"))
b = int(input("Enter second Number:"))
c = int(input("Enter third Number:"))

if a > b and a > c:
    print("Largest :",a)
elif b > a and b > c:
    print("Largest :",b)
else:
    print("Largest :",c)