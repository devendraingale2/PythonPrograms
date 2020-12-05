'''
      A
    B A 
  C B A
D C B A
'''
B=65
for i in range(4):
    A=B
    for space in range(4-i):
        print(" ",end=" ")

    for j in range(i+1):
        print(chr(A),end=" ")
        A-=1
    B+=1
    print()
