A=65
size=int(input("Enter Size:"))

for i in range(size,0,-1):
    for j in range(i):
        print(chr(A),end=" ")
    print()
    A+=1

