# 15. Perform union and update operations between two sets.

num1 = {1, 2, 3, 4, 5}
num2 = {4, 5, 6, 7, 8}

num1.union(num2)
print("Union of two sets:", num1.union(num2))

num3 = {11 ,18 ,19}
num1.update(num3)
print("Update of first set with second set:", num1)