num=int(input("Enter Value:"))

for outer in range(1,num+1):
    for space in range(num-outer):
        print(" ",end=" ")
    for inner in range(outer):
        print(num+1-outer+inner,end=" ")
    print()
