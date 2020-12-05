
def pat():
    m = 4
    r = 65
    for outer in range(1,5):
        for inner in range(m):
            print(" ",end=" ")
        m -= 1
        s = r
        for inner in range(outer):
            print(chr(s),end=" ")
            s -= 1
        r += 1
        l = 66
        for inner in range(outer-1):
            print(chr(l),end=" ")
            l += 1
        print()




pat()
