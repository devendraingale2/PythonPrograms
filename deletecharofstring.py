lst=[]
name=input("Enter the String:").split(" ")
for i in range(len(name)):
    for j in range(len(name[i])):
        lst.append(name[i][j])


n=0
n=int(input("Enter Character Location:"))
lst.remove(lst[n])
st=""
for i in lst:
    st=st+i
print("String after Deletion:",st)
