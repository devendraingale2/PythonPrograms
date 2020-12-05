a=0
b=1
for i in range(4):
    for j in range(i+1):
        c=a+b
        a=b
        b=c
        print(a,end=" ")
             

    print()
