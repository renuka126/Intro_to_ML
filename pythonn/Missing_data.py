import pandas as pd
import numpy as np
data =pd.read_csv("D:/Pandas_dataa/empp.csv")

#replaces all the nan values with the given input
print(data.replace(np.nan,3000))

data["salary"] = data["salary"].replace(np.nan ,3000)
print (data)
data["Name"]= data["Name"].replace(np.nan,"rudra")
print(" ")
print(data)
#to fill the data without changing the mean,
# fill the data with the mean value
print(" ")
print(data["salary"].mean())
print(" ")
#we can also fill the down valus into the vaccancy
data1 =pd.read_csv("D:/Pandas_dataa/empp.csv")
print(data1.ffill())  # forward fill
print(data1.bfill())  # backward fill

print(" ")





                                        