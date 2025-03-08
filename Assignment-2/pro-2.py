list = [1 , 3 , 1]
list1 = list.copy()
list.reverse()
if list1 == list:
    print("List is palindrome")
else:
    print("List is not palindrome")