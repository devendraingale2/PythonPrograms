num= input("Enter NUmber:")
rep=int(input("Enter Replacable:"))

lst=[]
for i in range(len(num)):
    lst.append(int(num[i]))

for i in range(len(lst)):
    if lst[i]==1:
        lst[i]=rep
print(lst)




