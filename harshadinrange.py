a=input("Enter Start:")
b=int(input("Enter End:"))
lst=[]
for j in range(int(a),b+1):
    sum1=0
    if len(str(j))==1:
        sum1+=j
    else:
        for i in range(len(str(j))):
                j=str(j)
                c=j[i]
                sum1=sum1+int(c)

    if int(j)%sum1==0:
        lst.append(int(j))

for i in lst:
    print(i,end=" ")



