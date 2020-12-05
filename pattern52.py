'''
5 4 3 2 1
  4 3 2 1
    3 2 1
      2 1 
        1
'''

a=5
b=5
for i in range(1,6):
    for space in range(i):
        print(" ",end=" ")
    for j in range(6-i):
        print(a,end=" ")
        a-=1
        
    a=b-1
    b=b-1
    print()

