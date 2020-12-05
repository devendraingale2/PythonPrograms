import numpy as np


def occurence(num,arr1):
    c=0
    for i in range(len(arr1)):
        if num==arr1[i]:
            c+=1

    print(num,"appeared",c,"times.")







list1=[]
list1=input("Enter Integers:").split(",")

arr1=np.array(list1,int)
print("Array Elements:",end=" ")
for i in arr1:
    print(i,end=" ")

num=int(input("\nEnter any number from array:"))
occurence(num,arr1)
