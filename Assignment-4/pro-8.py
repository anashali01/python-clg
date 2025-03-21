# Create a calculator that takes two numbers and an operator (+, -, *, /, //, %, **) as input
# and returns the result. (Terminate the program only after the user inputs “0”)
# Create a calculator that takes two numbers and an operator (+, -, *, /, //, %, **) as input
# and returns the result. (Terminate the program only after the user inputs “0”)
def calculator(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case '//':
            return num1 // num2
        case '%':
            return num1 % num2
        case '**':
            return num1 ** num2
        case _:
            return "Invalid operator"

while True:
    user_input = input("Enter '0' to exit or press Enter to continue: ")
    if user_input == '0':
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /, //, %, **): ")

    result = calculator(num1, num2, operator)
    print("Result:", result)