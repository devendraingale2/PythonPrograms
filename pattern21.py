'''
1
8 27
64 125 216
343 512 729 1000
'''

size=int(input("Enter Size:"))
a=1
for i in range(1,size+1):
    for j in range(i):
        print(a**3,end=" ")
        a+=1
    print()
