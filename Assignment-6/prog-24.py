# 24. Find the student with the highest marks.
student_data = {
    "daksh" : 90 ,
    "yash" : 89 , 
    "steave" : 79 ,
    "herobrine" : 99
}
print("Highest Marks in class :" , max(student_data , key = student_data.get))
