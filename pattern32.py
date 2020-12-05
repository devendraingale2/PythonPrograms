'''
      A
    A B C
  A B C D E
A B C D E F G
'''

a=8
c=0
A=65
for i in range(1,a+1):
    for j in range(1,(a-i+1)):
        print(end=" ")
    while c!=(2*i-1):
        print(str(chr(A)),end=" ")
        c=c+1
        A+=1
    c=0
    A=65
    print()
