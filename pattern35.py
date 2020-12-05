def pat():
    a = 4
    r = 68
    for outer in range (1,8,2):
        for space in range (a):
            print(" ",end=" ")
            r -= 1
        a -= 1
        for inner in range (outer):
            print(str(chr(r)),end=" ")
        print()
    a = 4
    r = 68
    for outer in range(5,0,-2):
        for space in range(6-a):
            print(" ",end=" ")
            r -= 1
        a -= 1
        for inner in range(outer):
            print(str(chr(r)),end=" ")
        print()

pat()


