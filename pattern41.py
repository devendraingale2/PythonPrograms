A=65
num=int(input("Enter Range:"))
for i in range(1,num+1):
    for space in range(num-i):
            print(" ",end=" ")
    for j in range(i):
        print(chr(A),end=" ")
        A+=1
    A=65
    print()
