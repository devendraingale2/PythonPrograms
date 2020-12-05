

set1 = set()
i = 1
for a in input("Enter value :").split():
    set1.add(a)
if(len(set1) % 2 == 0):
    print("Set is even")
else:
    print("Middle element is",end=" ")
    for a in set1:
        if i == len(set1)//2+1:
            print(a)
        i += 1
