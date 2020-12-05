'''
      =
    = A
  = B A
= C B A
'''

A=65
c=4
for i in range(5):
    for j in range(4,0,-1):
        if j==c:
            print("=",end=" ")
        elif j!=c:
            print(str(chr(A+i)),end=" ")
            
        c-=1
    a=65
    print()
