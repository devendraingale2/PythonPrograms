'''
            *
        *   *
    *   *   *
*   *   *   *
'''
a="*"
b=1
c=4
d=0
for i  in range(1,5):
    while(c>(i-1)):
        print(" ",end="\t")
        c-=1

    while(b>d):
        print(a,end="\t")
        b-=1
    
    c=4
    b=i+1
    print()
