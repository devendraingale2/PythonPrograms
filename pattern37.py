def pat():
    s = 1
    for outer in range(4,0,-1):
        for space in range(4-outer):
            print(" ",end=" ")
        l = s
        for inner in range(outer*2-1):
            print(l,end=" ")
            l += 1
        s += 1
        print()

pat()
