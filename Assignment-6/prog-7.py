# 7. Find all duplicate elements in a tuple.
movie = ("Inception", "The Matrix", "Interstellar" ,"Inception" , "Inception")
list = []
list2 = []

for movie in movie:
    if movie not in list:
        list.append(movie)
    else:
        list2.append(movie)

print("Duplicate elements in the tuple are: ", list2)