'''
0   1   10  11
    10  11  100
        100 101
            110
'''

a=0
c=0
binary=""
for i in range(1,5):
    for space in range(i):
        print(" ",end="\t")
    for j in range(5-i):
        binary=bin(a)
        print(binary[2:],end="\t")
        if j==2:
            c=a
        a+=1
    if i<3:
        a=c

    print()
