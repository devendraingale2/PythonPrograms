'''
+ = + =
+ = +
+ =
+
'''

a="+"
b="="
for i in range(4,0,-1):
    for j in range(i):
        if j%2!=0:
            print(a,end=" ")
        else:
            print(b,end=" ")
    print()

