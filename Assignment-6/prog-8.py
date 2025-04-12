# 8. Find the index of the first even number in a tuple.
number = (3 , 4 , 7 , 90 , 5 )

for i in number:
    if i % 2 == 0:
        print("The index of the first even number in the tuple is: ", number.index(i))
        break