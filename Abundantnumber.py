def Abundant(num):
    div=0
    for i in range(1,int(num/2)+1):
        if num%i==0:
            div+=i

    if div>num:
        print(num,"is an Abundant Number,since",div,"is greater than",num)
    else:
        print(num,"is not an Abundant Number,since",div,"is less than",num)




num=int(input("Enter A Number:"))
Abundant(num)
