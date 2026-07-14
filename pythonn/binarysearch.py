print("Binary and linear search")
print()
A= [ 10, 20, 30, 40,50]
key= int(input("Enter the value of key:"))

def linear_search(A,key):
    for i in range(0, len(A)):
        if(A[i]==key):
            print("Key is found through linear search")
            break
        else:
            print("Key is not found through the linear search")

def binary_search(A,key):
    low= 0
    high= len(A)-1
    for i in range(0, len(A)):
        
        mid= (low+high)//2
        if(A[mid]==key):
            print("Key is found through binary_search")
            break
        elif(A[mid]>key) :
            high=mid-1
        else:
            low=mid+1
        print("key is not found through binary search")   

linear_search(A, key) 
print()
binary_search(A, key)              

