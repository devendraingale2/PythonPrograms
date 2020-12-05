try:
    a=int(input("Enter A Number:"))
    fact=1
    count=1
    for i in range(1,a+1):
        fact=fact*count;
        count+=1
    print("Factorial of",a,"is:",fact)
except Exception as ve:
    print("Enter Valid Integer Number..!!")
    print(ve)
