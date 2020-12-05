'''
          3
      3   12
   3  8   15
3  4  10  18
'''
a=12
b=0
x=0
c=15
d=18
for i in range(1,5):
    for space in range(5-i):
        print(" ",end=" ")
    print("3",end=" ")
    for j in range(i-1):
        if j==0:
            print(a-b,end=" ")
            b+=4
        if j==1:
            print(c-x,end=" ")
            x+=5
        if j==2:
            print(d,end=" ")
    print()
