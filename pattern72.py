'''
1 2 3 4 5 6 7
  2 3 4 5 6 
    3 4 5 
      4

'''

A=1
a=3
b=1
c=0
for i in range(4):
    for space in range(i):
        print("  ",end="")
    for j in range(c+i,7-i):
        print(A,end=" ")
        A+=1
    
    
    b+=1
    A=b
    print()
