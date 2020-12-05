'''
1
4 9
16 25 36 
49 64 81 100
'''


size=int(input("Enter Size:"))
a=1
for i in range(1,size+1):
    for j in range(i):
        print(a**2,end=" ")
        a+=1
    print()
