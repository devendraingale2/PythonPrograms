lst3=[]
lst1=[]
lst2=[]
print("Enter First Array:")
for i in range(5):
    lst1.append(int(input()))

print("Enter Second Array:")
for i in range(5):
    lst2.append(int(input()))
lst3=lst1+lst2
print("Array After Concatenation:",lst3)

for i in range(len(lst3)):
    for j in range(i):
        if lst3[i]==lst3[j]:
            lst3[i]=0


print("Array After replacing 0 for repetation:",lst3)

