a=1
b=1
for i in range(4):
    print(b,end=" ")
    for j in range(3):
        a=a+1
        print(a,end=" ")
        b=a
        if(a==4):
            a=0

    print()
