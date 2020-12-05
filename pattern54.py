

s = 69
r = 97
for i in range(1,5):
    for j in range(1,5):
        if(i<=j):
            if(j %2 != 0):
                print(chr(s),end=" ")
                s -= 1
            else:
                print(chr(r),end=" ")
                r += 1
        else:
            print(" ",end=" ")
    print()

