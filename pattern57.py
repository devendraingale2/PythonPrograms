'''
0   0   0   0   0
    1   2   3   4
        2   4   6
            9   12
                16
'''
b=0
a=[0,1,2,3,4]
for i in range(1,6):
    for space in range(i):
        print(" ",end="\t")
    for j in range(6-i):
        print(a[i-1]*b,end="\t")
        b+=1
    b=i 
    print()
