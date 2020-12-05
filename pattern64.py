'''
A B D G
G H J
J K 
K
'''
A=65
b=1
C=0
for i in range(4):
    for j in range(4-i):
        if j==(4-i-1):
            C=A
        print(chr(A),end=" ")
        A+=b
        b+=1
    A=C
    b=1
    print()

