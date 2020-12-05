'''
1
1 2 
1 2 3
1 2 3 4
1 2 3
1 2
1
'''
a=1
for i in range(4):
    for j in range(i+1):
        
        print(a,end=" ")
        a+=1

    a=1
    print()
x=3
for k in range(3):
    for l in range(x,0,-1):
        
        print(a,end=" ")
        a+=1
    x-=1
    a=1
    print()

