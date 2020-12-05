#BinaryTo HExadecimal for 8Bit Binary Only..!!

import numpy as np


list1=[]
list2=[]
print("Enter Binary no one by one(upto 8bits):")
for i in range(0,8):
    elements=int(input())
    if i<4:
        list1.append(elements)
    if i>3:
        list2.append(elements)

print("List1=",list1)
print("List2=",list2)
arr=np.array(list1,int)
a=8
c=0
for i in range(4):
    c=c+(arr[i]*a)
    a=a/2
print(c)


arr2=np.array(list2,int)
d=8
e=0
for i in range(4):
    e=e+(arr2[i]*d)
    d=d/2
print(e)

for i in range(1,16):
    if i <10:
        if c==i:
            ch=str(i)
    if c==10:
        ch="A"
        break
    if c==11:
        ch="B"
        break
    if c==12:
        ch="C"
        break
    if c==13:
        ch="D"
        break
    if c==14:
        ch="E"
        break
    if c==15:
        ch="F"
        break
for i in range(1,16):
    if i <10:
        if e==i:
            ch1=str(i)
    if e==10:
        ch1="A"
        break
    if e==11:
        ch1="B"
        break
    if e==12:
        ch1="C"
        break
    if e==13:
        ch1="D"
        break
    if e==14:
        ch1="E"
        break
    if e==15:
        ch1="F"
        break

hexa=str(ch)+str(ch1);
print("Hexadecimal Is:",hexa)
