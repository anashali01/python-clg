# Create an inverted dictionary where values become keys and keys become grouped in a list.

dict1= {
    "num1": 1,
    "num2": 2,
    "num3": 3,
    "num4": 4
}
dict2 = {}
for key, value in dict1.items():
    if value not in dict2:
        dict2[value] = [key]
    else:
        dict2[value].append(key)
print(dict2)