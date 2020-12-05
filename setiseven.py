def setf(set1):
    c=(len(set1))
    if c%2==0:
        print("Set Is Even")
    else:
        mid=round(c/2)
        for i in set1:
            x=1
            if x==mid:
                print(i)
            x+=1



set1={()}
list1=[]
list1=input("Enter Inputs:").split(",")
for i in list1:
    set1.add(i)
for j in set1:
    print("Set Elements Are:",j)
setf(set1)
