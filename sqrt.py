num=int(input("Enter Number:"))
flag=0
for i in range(1,num+1):
    if (i**2==num):
        print("Square Root Of",num,"is:",i)
        flag=1
        break
    else:
        flag=0

if flag==0:
    print("Not A Perfect Square.")
