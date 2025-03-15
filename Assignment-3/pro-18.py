# Using break and continue statements
i = 0
while i < 10:
    if i == 3:
        break  # Exit the loop when i is 3
    elif i == 5:
        i += 1
        continue  # Skip the rest of the loop when i is 5
    else:
        print(i)
    i += 1
