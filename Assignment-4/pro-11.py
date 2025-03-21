def longest(s):
    s1 = s.split(" ")
    l = str(max(s1 , key=len))
    print(l)
s = input("Enter str:")
longest(s)