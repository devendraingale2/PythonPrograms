'''
        9
     9  16
  9  16 25
9 16 25 36
'''

a=3
for i in range(1,5):
    for space in range(5-i):
        print(" ",end="\t")

    for j in range(i):
        print(a**2,end="\t")
        a+=1

    a=3
    print()
