try:
    pamount=float(input("Enter Principle Amount:"))
    rate=float(input("Enter Rate Of Interest:"))
    time=float(input("Enter Number of Years:"))

    sinterest=(pamount*rate*time)/100

    print("The Simple Interest Is:",sinterest)
except ValueError:
    print("Exception Raised:Enter Valid Integer Values..!!")
