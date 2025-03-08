list = [2 , 4 , 6 , 9 , 9 , 9]
num = int(input("Enter number which u want to find:"))
count = 0
i = 0
while i < len(list):
    if(num == list[i]):
        print(list[i])
        count += 1
    else:
        print("Finding")

    i+=1
print("The number of repeat",count)