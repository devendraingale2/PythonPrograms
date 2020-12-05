def AP(start,num,diff):
    print("AP is:",end=" ")
    for i in range(num):
        print(start,end=" ")
        start+=diff




start=int(input("Enter Starting Element:"))
diff=int(input("Enter Common Difference:"))
num=int(input("Enter Number Of Elements:"))
AP(start,num,diff)
print()
