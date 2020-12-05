

def Perfect(num1):
    sum1 = 0
    for i in range(1,num1):
        if(num1 % i == 0):
            sum1 = sum1 + i
    return sum1

flag=1
while flag==1:
    num1 = int(input("Enter No: "))
    if (num1 == Perfect(num1)) or num1==1:
        flag=1
    else:
        print("Terminating..!!")
        flag=0
        exit()
