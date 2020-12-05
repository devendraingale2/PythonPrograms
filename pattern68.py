'''
       *
     * * *
   * * * * *
 * * * * * * *
'''
A="*"
a=0
for i in range(1,5):
    for space in range(4-i):
        print(" ",end=" ")
    for j in range(i+a):
        print(A,end=" ")
    a+=1
    print()
