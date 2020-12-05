num=int(input("Enter Range:"))
print("Disarium Numbers in(",1,num,"):",end=" ")
for j in range(1,num+1):
    l=0
    for i in range(len(str(j))):
        l+=(int(str(j)[i])**(i+1))

    if l==int(j):
        print(j,end=" ")

print()
