'''
*
*   *   
*   *   *
*   *   *   *
'''

a="*"
b=0
for i in range(4):
    while(b<i+1):
        print(a,end="\t")
        b+=1
    b=0
    print()
