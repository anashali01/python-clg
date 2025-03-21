# Write a program that takes an integer input and uses assignment operators (+=, -=, *=,
# /=, //=, %=) to modify it and print the result after each operation sequentially.
num = int(input("Enter an integer: "))
print("Original number:", num)
num += 5
print("After adding 5:", num)
num -= 5
print("After subtracting 5:", num)
num *= 5
print("After multiplying by 5:", num)
num /= 5
print("After dividing by 5:", num)
num //= 5
print("After floor dividing by 5:", num)
num %= 5
print("After taking the remainder by 5:", num)