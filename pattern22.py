'''
3
2 3
1 2 3
0 1 2 3
'''

a=int(input("Enter Size:"))
b=a
for i in range(a):
    for j in range(i+1):
        if b<a+1:
            print(b,end=" ")
            b+=1
        elif b>5:
            break
    b=a-i-1
    print()

