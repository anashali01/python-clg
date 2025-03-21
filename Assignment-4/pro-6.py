# Write a program that validates a password using the following rules:
# ● It must be at least 8 characters long.
# ● It must contain at least one uppercase letter, one lowercase letter, and one number.
# ● It should not contain spaces. Use string methods and logical operators.
def passwordValidator(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if ' ' in password:
        return False
    return True

password = input("Enter your password: ")

if passwordValidator(password):
    print("Password is valid.")
else:
    print("Password is invalid.")