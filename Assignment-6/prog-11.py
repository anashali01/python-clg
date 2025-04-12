# 11. Find a pair of numbers in a tuple that add up to a target sum.

number = (1, 2, 3, 4, 5, 6, 7, 8, 9 , 10)
target_sum = 10
# i=0
# while i < len(number):
#     j=0
#     while j < len(number):
#         if number[i] + number[j] == target_sum:
#             print("The pair of numbers that add up to the target sum are: ", number[i], "and", number[j])
#         j+=1
#     i+=1
for i in range(len(number)):
    for j in range(i + 1, len(number)):
        if number[i] + number[j] == target_sum:
            print("The pair of numbers that add up to the target sum are: ", number[i], "and", number[j])