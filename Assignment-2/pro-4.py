list = [2 , 4 , 6 , 9]
num = int(input("Enter number which u want to find:"))
i = 0
while i < len(list):
    if(num == list[i]):
        print(list[i])
        break
    else:
        print("Finding")

    i+=1