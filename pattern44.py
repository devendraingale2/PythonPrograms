for outer in range(1,5):
    l = 65
    for space in range(4-outer):
        print(" ",end=" ")
        l += 1
    s = l
    for inner in range(outer):
        print(chr(s),end=" ")
        s += 1
    print()
