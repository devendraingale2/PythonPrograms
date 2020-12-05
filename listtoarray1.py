from array import *

list1=["Devendra","Jockey","RockStar","Jazz"]
print("Lst 1:",list1)
list2=["Dev","Master","DJRJ","DJ","MJ"]
print("List 2:",list2)
list3=[]

for i in list1:
    list3.append(i[0])
print("List 3:",list3)



arr=array('u',list3)
print("Array 1:",end=" ")
for a in arr:
    print(a,end=" ")

print()



str = ""
print("String:",end=" ")
for i in list3:
    str = str + i
print(str,end=" ")
print()



index=0
for i in list2:
    if (str==(i)):
        print("Element",str,"found at Index:",index)
        index+=1
    else:
        index+=1
