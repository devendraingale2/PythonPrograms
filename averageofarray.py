
from array import *


arr1 = array('i',[])
arr2 = array('i',[])

for a in input("Enter arr1 : ").split():
    arr1.append(int(a))
for a in input("Enter arr2 : ").split():
    arr2.append(int(a))
sum = 0
for a in arr1:
    sum += a
avg = sum/len(arr1)

for a in arr2:
    if(avg == a):
        print("Average of Array1 {} is available in Array2".format(avg))
    else:
        print("Not found")
        
