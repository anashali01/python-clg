# 21. Access and remove an element from the dictionary.
student_data = {
    "daksh" : 90 ,
    "yash" : 89 , 
    "steave" : 79 ,
    "herobrine" : 99
}

print("Student Data:", student_data["yash"])

student_data.pop("steave")
print("After removing 'steave':", student_data)