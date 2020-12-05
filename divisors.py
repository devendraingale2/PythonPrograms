try:
    a=int(input("Enter Number:"))
    print("Diviors of",a,"are:",end=" ")
    for i in range(1,a+1):
        if a%i==0:
            print(i,end=" ")
    print()
except Exception:
    print("Enter Valid Integer..!!")
