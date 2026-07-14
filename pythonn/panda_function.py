import numpy as np
import pandas as pd

lisa = [2 ,4 ,5  ]
array = np.array(lisa , dtype= float)
#print(len(lisa))
#print(array.ndim)

array2 = np.array([[3,4,5],[3,4,5]])
#print(array2.ndim)

data = {"Name": ["John", "Peter", "Lisa"], 
        "Age" : [24,26,23],
        "Salary":[30000, 45000, 38000]}

print(" ")
df = pd.DataFrame(data)
print(df)
print(" ")
#importing the csv file
data2 = pd.read_csv("D:/Pandas_dataa/numm.csv")
print(data2)
data4 = pd.read_csv("D:/Pandas_dataa/num_empty.csv")

print(" ")
#importing the exel file
data3 = pd.read_excel("D:/Pandas_dataa/numm2.xlsx")
print(data3)
print(" ")

#for printing the starting and ening few records
print(data2.head(5))
print(" ")
print(data2.tail(5))
print(" ")
#for knowing the info of the table rows, columns , datatype
#print(data) gives an error as the dict not has info function
print(data3.info())
print(data2.info)

print(" ")
#describe the table about the data present
#data.describe ...not works for the dict
data2.describe()
 
#isnull function is used to show if the cell is empty or not
#it replaces the value with the true and false
print(" ")
print(data2.isnull)
print(data4.isnull) 
#isnull().sum() function tells the number of empty cells
print(data4.isnull().sum())
print(" ")
#shows if duplicate data is present pr not
#prints true or false as output
print(data4.duplicated())

#removes all the dublicates values and only unique values are shown
print(" ")
print(data3.drop_duplicates("days"))

#delets the record having the null values
print(data4.dropna())




