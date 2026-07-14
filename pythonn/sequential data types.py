samarr = (3 , 6, 4 )
listt = [3 ,4 , 6]
spyder = "String" , "Boot"
x = "Hello Dear"
y = range(6)
abcc = { 3: "Jan" , "Feb": "love"}
sett = { "Tom" ,3, "Jack"}
lisa = [ 4 , 'renu']
sam = ( 4 , "renu")
print (abcc[3])
print ( abcc["Feb"])
rangesample = range(1, 12, 4)
print(rangesample)
for i in  rangesample: print(i)
print(" ")

lstsam = [1 , 2 , 'a', "renu" , "pari"]
print(lstsam[-3:-1])
print(sett)
sett.clear()
print(sett)
sett.add(3)
sett.update([4])
print(sett)
sett.update(["RENU"])
print(sett)
sett.update("RENU")

print(sett)
import numpy as np
array = np.array(abcc)
arr2 = np.array(2 )
print(" ")
print("ARITHMETIC OPERATIONS ")
print(" ")
a= np.array([[1,2],[3,4]], dtype = np.int8)
b= np.array([[5,6],[6,8]], dtype= np.int8)
print(a.dot(b))
print(np.dot(a,b))
print(np.sum(a))
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))