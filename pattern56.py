'''

C   O   R   E
    O   R   E
        R   E
            E

'''

word=['C','O','R','E']
a=0
for i in range(1,5):
    for space in range(i):
        print(" ",end="\t")
    for j in range(5-i):
        print(word[a],end="\t")
        a+=1
    a=i
        

    print()
