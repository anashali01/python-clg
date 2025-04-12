# 10. Check if two tuples are anagrams (same elements in different order).
number_1 = (1, 2, 3, 4, 5)
number_2 = (5, 4, 3, 2, 1)

if sorted(number_1) == sorted(number_2):
    print("The tuples are anagrams.")
else:
    print("The tuples are not anagrams.")
    