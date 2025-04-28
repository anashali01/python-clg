import numpy as np
from scipy import stats as st

number = np.array([12,15, 12, 18, 21, 24, 24, 24, 27, 30]) 

print("Mean of number :",np.mean(number))

print("Median of number :",np.median(number))

print("Mode of number :",st.mode(number))

print("Standard Deviation :" ,np.std(number))

print("Variance :",np.var(number))