# 14. Use set methods: add(), clear(), copy(), discard(), pop(), remove().

data = {"apple", "banana", "cherry"}
print("Original set:", data)

data.add("orange")
print("After add:", data)

data.clear()
print("After clear:", data)

data = {"apple", "banana", "cherry" , "orange" , "grape" , "kiwi"} 
copy_data = data.copy()
print("Copy of set:", copy_data)

data.discard("banana")
print("After discard:", data)

data.pop()
print("After pop:", data)

data.remove("cherry")
print("After remove:", data)