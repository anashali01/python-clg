#WAP to create a user define function and perform separate arithmetic Operator.

def add(num1 , num2):
    ans=num1 + num2
    print(ans)
def sub(num1 , num2):
    ans = num1 - num2
    print(ans)
def mul(num1 , num2):
    ans = num1 * num2
    print(ans)
def div(num1 , num2):
    ans = num1 / num2
    print(ans)
def mod(num1 , num2):
    ans = num1 % num2
    print(ans)

print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for divison")
print("Enter 5 for modulus")
choice = int(input("Choice ="))
if choice == 1:
    num1 = int(input("Enter number1:"))
    num2 = int(input("Enter number2:"))
    add(num1 , num2)
elif choice == 2:
    num1 = int(input("Enter number1:"))
    num2 = int(input("Enter number2:"))
    sub(num1 , num2)
elif choice == 3:
    num1 = int(input("Enter number1:"))
    num2 = int(input("Enter number2:"))
    mul(num1 , num2)
elif choice == 4:
    num1 = int(input("Enter number1:"))
    num2 = int(input("Enter number2:"))
    div(num1 , num2)
elif choice == 5:
    num1 = int(input("Enter number1:"))
    num2 = int(input("Enter number2:"))
    mod(num1 , num2)
