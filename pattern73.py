'''
1 2 3 4 5 6 7
  7 6 5 4 3  
    3 4 5 
      5

'''

A=1
a=3
b=1
c=0
for i in range(4):
    for space in range(i):
        print("  ",end="")
    if i%2==0:    
        for j in range(c+i,7-i):
            print(A,end=" ")
            A+=1
    if i%2!=0:
        for j in range(7-i,c+i,-1):
            print(A,end=" ")
            A+=1

    
    
    b+=1
    A=b
    print()
