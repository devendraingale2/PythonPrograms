'''
            100
        81  64
    49  36  25
16  9   4   1

'''
a=10
for i in range(1,5):
    for space in range(5-i):
        print(" ",end="\t")
    for j in range(i):
        print(a**2,end="\t")
        a-=1
    print()
