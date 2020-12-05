import numpy as np
    
def add(arr1,arr2,list3):
    for i in range(len(arr1)):
            list3.append(arr1[i]+arr2[i])
    
    arr3=np.array(list3,int)
    print("Elements Of Array 3 are:",end=" ") 
    for i in arr3:
        print(i,end=" ")



list1=[]
list1=input("Enter Array 1 Elements:").split(",")
list2=[]
list2=input("Enter Array 2 Elements:").split(",")

arr1=np.array(list1,int)
arr2=np.array(list2,int)
list3=[]
add(arr1,arr2,list3)
