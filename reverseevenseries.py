
def even(num):
    for i in range(num,0,-1):
        if i%2==0:
            print(i,end=" ")



num=int(input("Enter Range:"))
even(num)
print()
