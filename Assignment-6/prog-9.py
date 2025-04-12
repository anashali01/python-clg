# 9. Swap two values in a tuple (e.g., first and third).
movie = ("Superman" , "MortalKombat" , "Batman" , "SpiderMan")

print("Before swapping: ", movie)

movie_list = list(movie)

movie_list[1] = movie[2]
movie_list[2] = movie[1]

movie_tuple = tuple(movie_list)

print("After swapping: ", movie_tuple)