def AP(limit,cd):
    while(limit!=0):
        print(limit,end=" ")
        limit-=cd


limit=int(input("Enter last Digit:"))
cd=int(input("Enter Common Difference:"))
AP(limit,cd)
print()
