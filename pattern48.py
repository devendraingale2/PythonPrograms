'''

            A3
        B3  A4
    C3  B4  A5
D3  C4  B5  A6
'''

A=65
a=3
B=65
for i in range(1,5):
    for space in range(5-i):
        print(" ",end="\t")

    for j in range(i):
        print(chr(A)+str(a),end="\t")
        A-=1
        a+=1
    B+=1
    A=B
    a=3
    print()
