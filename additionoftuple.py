def addtuple(tuple1):
    a=0
    for i in tuple1:
        a=a+int(i)
    print("\nAddition Of Tuple Elements:",a)

tuple1=()
tuple1=input("Enter Integers:").split(",")
for i in tuple1:
    i=int(i)
print("Elements of Tuple:",end=" ")
for i in tuple1:
    print(i,end=" ")
addtuple(tuple1)
