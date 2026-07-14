import numpy as np
import pandas as pd

lisa = [2 ,4 ,5  ]
array = np.array(lisa , dtype= float)
print(len(lisa))
print(array.ndim)

array2 = np.array([[3,4,5],[3,4,5]])
print(array2.ndim)

data = {"Name": ["John", "Peter", "Lisa"], 
        "Age" : [24,26,23],
        "Salary":[30000, 45000, 38000]}

print(" ")
df = pd.DataFrame(data)
print(df)
print(" ")

data2 = pd.read_csv("D:/Pandas_dataa/numm.csv")
print(data2)

print(" ")

data3 = pd.read_excel("D:/Pandas_dataa/numm2.xlsx")
print(data3)