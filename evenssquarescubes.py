try:
    def evencubesquare(start,last):
        for i in range(start,last+1):
            if i%2==0:
                print("Square of",i,"is",i**2,"\tCube of",i,"is",i**3)

    start=int(input("Enter Starting Number:"))
    last=int(input("Enter Ending Number:"))
    evencubesquare(start,last)

except Exception:
    print("Enter Valid Integer..!!")
