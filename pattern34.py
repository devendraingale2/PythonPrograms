'''
7 14 21 35 
42 49 56
63 28
70
'''

k = 1
for outer in range(4,0,-1):
    for inner in range(outer):
        print(7*k,end=" ")
        k += 1
    print()
