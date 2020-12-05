try:
    def factorial(start,end):
        fact=1
        for i in range(start,end+1):
            fact=fact*i
            print("Factoria of",i,"is:",fact)
        

    start=int(input("Enter starting number:"))
    end=int(input("Enter Ending number:"))
    factorial(start,end)

except Exception:
    print("Enter Valid Integer..!!")
