import numpy as np
from scipy import stats as st

list = [10 , 20 , 90 , 66 , 54]

print("List :" , list)

arr = np.array(list)

print("The original array :" , arr)

print("Mean of number :",np.mean(arr))

print("Median of number :",np.median(arr))

print("Mode of number :",st.mode(arr))

print("Standard Deviation :" ,np.std(arr))

print("Variance :",np.var(arr))