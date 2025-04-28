# WAP perform arithemetic opreation using UDF
def arithmetic(num1 , num2):
    print(f"{num1} + {num2} = " , num1+num2)
    print(f"{num1} - {num2} = " , num1-num2)
    print(f"{num1} x {num2} = " , num1*num2)
    print(f"{num1} / {num2} = " , num1/num2)
    print(f"{num1} % {num2} = " , num1%num2)

num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))

arithmetic(num1 , num2)