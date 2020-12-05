try:
    total=0
    a=int(input("Enter A Number:"))
    for i in range(1,a+1):
        total=total+i
    print("Sum Of Numbers Upto",a,"Is:",total)
except Exception :
    print("Enter Valid Natural Number..!!!")
