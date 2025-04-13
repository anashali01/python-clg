# Remove duplicate dictionaries from a list based on a key.

dict_list = [
    {"name": "anash", "age": 30},
    {"name": "kane", "age": 25},
    {"name": "anash", "age": 30},
    {"name": "Don", "age": 22}
]

unique_dicts = {frozenset(d.items()): d for d in dict_list}.values()
print(list(unique_dicts))