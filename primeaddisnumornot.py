
def primeno(x):
    global l
    if x>1:
        
        for i in range(2,x):
            if (x%i)==0:
                break;
        else:
            l.append(x)

x=int(input("Enter Number:"))
l=[]
for i in range(x+1):
    primeno(i)
for i in range(len(l)):
    for j in range(i+1):
        if l[i]+l[j]==x:
            print(l[i],"+",l[j],"gives",x)
print()
