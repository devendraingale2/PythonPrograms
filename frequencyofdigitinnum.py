num=input("Enter Number:")
list1=[]
for i in range(len(num)):
    list1.append(num[i])

count=0
for i in list1:
    count=list1.count(i)
    print("Frequency of",i,"is:",count)
