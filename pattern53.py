'''
0 1 4 9 16
  1 6 12 20
    8 15 24
      18 28
         32
'''

a=0
b=0
for i in range(1,6):
    for space in range(i):
        print(" ",end="\t")
    for j in range(6-i):
        print(a,end="\t")
        b+=1
        a=b**2
    a=b+1
    print()

  
