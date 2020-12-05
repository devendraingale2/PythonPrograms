import array as arr
a=input("Insert List Values in Row:").split(" ")

for i in a:
    i=int(i)
    print(i)
z=arr.array('u',a)
for i in z:
    print(i)
