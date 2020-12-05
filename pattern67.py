'''
0 1 0 1
0 1 0 
0 1 
0
'''

a=0
b=1
for i in range(4):
    for j in range(4-i):
        if j%2==0:
            print(a,end=" ")
        else:
            print(b,end=" ")

    print()
