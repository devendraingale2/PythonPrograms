'''
7
6 5
5 4 3
4 3 2 1
'''
c=0
for i in range(1,5):
    a=7-c
    for j in range(i):
        print(a,end=" ")
        a-=1
    c+=1
    print()
