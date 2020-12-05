
list1=[]
list=input("Enter Number:")
for i in range(len(list)):
    list1.append(int(list[i]))


c=list1.count(1)
print("Occurence of 1 in",list1,"is:",c)
