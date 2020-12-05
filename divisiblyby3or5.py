try:
    a=int(input("Enter Start Number:"))
    b=int(input("Enter Ending Number:"))
    print("Numbers from ",a,"and ",b,"which are divisible By 3 or 5 are:")

    for i in range(a,b+1):
        if (i%3==0 or i%5==0):
            print(i,end=" ")
        
    print()
except Exception:
    print("Enter Valid Integers..!!")
