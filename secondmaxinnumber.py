num=input("Enter Number:")
lst=[]
for i in range(len(num)):
    lst.append(int(num[i]))
lst.remove(max(lst))
print("Second Maximum Value in",num,"is:",max(lst))
