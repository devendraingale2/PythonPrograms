import numpy as np

list=[]
list=input("Enter numbers:").split(" ")
print("\nBefore Reverse:",end=" ")
for i in list:
    print(i,end=" ")
list.reverse()
arr=np.array(list,int)
print("\nReverse Array:",end=" ")
for i in arr:
    print(i,end=" ")

print()
