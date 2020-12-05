'''
0A 1B 2C 3D
1A 2B 3C
2A 3B
3A
'''

A=65
b=0
c=0
for i in range(4):
    for j in range(4-i):
        print(str(b)+chr(A),end=" ")
        b+=1
        A+=1
    c+=1
    b=c
    A=65
    print()
