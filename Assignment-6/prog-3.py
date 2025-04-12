# 3. Replace an element in a tuple (convert to list and back).

movie = ("Inception", "The Matrix", "Interstellar")

print(movie)

menu = list(movie)

menu[2]=("The Dark Knight")

movie_menu = tuple(menu)

print(movie_menu)