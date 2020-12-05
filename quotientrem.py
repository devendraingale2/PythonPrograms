try:
    def Calc(ddend,dvsor):
        quo=ddend/dvsor
        rem=ddend%dvsor
        print("Quotient Is:",quo)
        print("Remainder Is:",rem)

    ddend=float(input("Enter Dividend:"))
    dvsor=float(input("Enter Quotient:"))
    Calc(ddend,dvsor)

except Exception as ve:
    print("Enter Valid Integers..!!\n",ve)
