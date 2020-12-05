'''
      D
    C D E
  B C D E F
A B C D E F G

'''

A=68
a=3
b=68
for i in range(1,5):
    for space in range(5-i):
        print(" ",end=" ")
    for j in range((a-i+1),(a+i)):
        print(chr(A),end=" ")
        A+=1
    
    b-=1
    A=b
    print()
