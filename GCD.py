try:
    num1=int(input("Enter Number1:"))
    num2=int(input("Enter Number2:"))
    min1=min(num1,num2)
    for i in range(min1,0,-1):
        if (num1%i==0 and num2%i==0):

            print("The GCD of",num1,"and",num2,"is:",i)
            break

except Exception:
    print("Enter Valid Integers..!!")

