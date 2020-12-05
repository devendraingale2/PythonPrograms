try:
    a=int(input("Enter a Number:"))
    for i in range(1,a+1):
        print("Cube of",i,"is:",i**3)

except Exception:
    print("Error:Invalid Integer Entered..!!")

