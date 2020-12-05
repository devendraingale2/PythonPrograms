num=input("Enter Number:")
lst=[]
for i in range(len(num)):
    lst.append(int(num[i]))
lst.remove(min(lst))
print("Second Minimum Value in",num,"is:",min(lst))
