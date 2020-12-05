
def pattern():
    m = 4
    for outer in range(1,5):
        r = 65
        for space in range(m):
            print(" ",end=" ")
        m -= 1
        for inner in range(outer):
            print(chr(r),end=" ")
            r += 1
        for inner in range(outer-1):
            print(chr(r),end=" ")
            r += 1
        print()

pattern()
