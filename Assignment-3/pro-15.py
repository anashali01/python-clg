age = int(input("Enter your age :"))
citizen = input("Are you citizen or not (yes / no):")
if age >= 18:
    if citizen == 'yes':
        print("You are eligible")
    else:
        print("You are not eligible")
else:
    print("Age is not eligible")