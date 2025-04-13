# 22. Use dictionary methods: get(), pop(), popitem(), clear(), copy().
data_dict ={
    "name" : "Kylie", 
    "age" : 25,
    "city" : "New York",
    "job" : "Engineer"
}

print("Original Dictionary:", data_dict)
print("Get method :" , data_dict.get("name"))

print("Pop method :" , data_dict.pop("age"))
print("After pop method:", data_dict)

print("Popitem method :" , data_dict.popitem())
print("After popitem method:", data_dict)

print("Clear method :" , data_dict.clear())
print("After clear method:", data_dict)

data_dict ={
    "name" : "Kylie", 
    "age" : 25,
    "city" : "New York",
    "job" : "Engineer"
}

copy_data = data_dict.copy()
print("Copy method :" , copy_data)
print("After copy method:", data_dict)

