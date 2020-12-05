
flag=1
while(flag==1):
    num=int(input("Enter Number:"))
    if num%7==0:
        flag=0
        print("Num Divisible by 7..Hence Exiting...!!")
        exit()
    else:
        print(num)


