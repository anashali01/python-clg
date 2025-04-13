# 20. Add a new student and their marks to the dictionary.
student_data = {
    "daksh" : 90 ,
    "yash" : 89 , 
    "steave" : 79 ,
    "herobrine" : 99
}
print("Student marks dictionary:", student_data)

new_student = input("Enter the name of the new student: ")
new_marks = int(input("Enter the marks of the new student: "))

student_data[new_student] = new_marks
print("Updated student marks dictionary:", student_data)