# 4. Add and remove elements in a tuple using conversion.

movie = ("Inception", "The Matrix", "Interstellar")

print(movie)

menu = list(movie)

menu.append("The Dark Knight")
menu.remove("Inception")

movie_menu = tuple(menu)

print(movie_menu)   