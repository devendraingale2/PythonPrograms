'''
      =
    = 1
  = 1 2
= 3 5 8
'''

a=1
b=0
list=[]
count=0
for i in range(1,7):
    c=a+b
    list.append(c)
    a=b
    b=c
for i in range(1,5):
    for space in range(5-i+1):
        print(" ",end=" ")
    print("=",end=" ")
    for j in range(i-1):
        print(list[count],end=" ")
        count+=1
    print()
