try:
    a=int(input("Enter Starting Number:"))
    b=int(input("Enter Ending Number:"))

    for i in range(a,b+1):
        if i%2==0:
            print(i,end = " ")
        else:
            continue
    print()
except Exception:
    print("Enter Valid Input..!!")

