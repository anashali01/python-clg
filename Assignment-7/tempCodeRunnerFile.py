import numpy as np
l = [
    [75,85,90],
    [85,98,95],
    [90,84,72],
    [76,90,94],
    [90,70,75]
]
arr=np.array(l)
print("Original array:")
print(arr)
student_avg=np.mean(arr, axis=1)
print("Student average:",student_avg)
subject_avg=np.mean(arr, axis=0)
print("Subject average:",subject_avg)
h_subavg=np.max(subject_avg)
print("Highest subject average:",h_subavg)