def fact(num):
    if int(num)==1:
        return 1
    else:
        return int(num)*fact(int(num)-1)



num=input("Enter Number:")

for i in range(len(num)):
    print("Factorial of",int(num[i]),"is:",fact(num[i]))
