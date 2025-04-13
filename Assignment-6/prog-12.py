# 12. Count frequency of elements in a tuple and store in a dictionary.
tuple_data = tuple(input("Enter elements separated by space: ").split(','))

frequency = {}

for item in tuple_data:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
        
print("Frequency of elements in the tuple:", frequency)