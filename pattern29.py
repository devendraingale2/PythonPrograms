'''
100
81 64
49 36 25
16 9 4 1
'''
a=10
for i in range(4):
    for j in range(i+1):
        print(a**2,end="\t")
        a-=1
    print()
