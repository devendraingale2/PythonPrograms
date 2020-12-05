from numpy import *

arr = array([])
for a in input("Enter value : ").split():
    arr.append(a)

for a in arr:
    count = 0
    for b in arr:
        if(a==b.reverse()):
            count += 1
    if(count != 0):
        print("Reverse string of {} appeared {} times".format(a,count))
