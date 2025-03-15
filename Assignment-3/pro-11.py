# Logical operators: and, or, not

a = 10
b = 5
c = 0

# and operator
result_and = (a > b) and (b > c)
print(f"({a} > {b}) and ({b} > {c}) = {result_and}")

# or operator
result_or = (a > b) or (b < c)
print(f"({a} > {b}) or ({b} < {c}) = {result_or}")

# not operator
result_not = not (a > b)
print(f"not ({a} > {b}) = {result_not}")

