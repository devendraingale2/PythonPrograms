a = int(input("Enter value : "))
flag = False
for num in range(1,a+1):
    for b in range(2,num):
        if(num % b != 0):
            flag = True
        else:
            flag = False
            break
    if(flag == True):
        print(num,end=" ")
