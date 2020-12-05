
def pat():
    l = 64
    for outer in range(1,5):
        for space in range(4-outer):
            print(" ",end=" ")
        print("=",end=" ")
        s = l
        for inner in range(outer-1):
            print(chr(s),end=" ")
            s -= 1
        l += 1
        print()


pat()
