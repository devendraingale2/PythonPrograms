flag=1
while(flag==1):
    num=int(input("Enter number:"))
    if num<0:
        flag=0
    else:
        print("Its Cube:",num**3)
else:
    print("Negatives Not allowed.")
