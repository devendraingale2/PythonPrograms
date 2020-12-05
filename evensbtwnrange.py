try:
    def evenno(start,end):
        print("Even Numbers between",start,"&",end,"are:")
        for i in range(start,end+1):
            if i%2==0:
                print(i,end=" ")

    start=int(input("Enter Starting Number:"))
    end=int(input("Enter Ending Number:"))
    evenno(start,end)

    print()     
           
except Exception:
    print("Enter valid Integer..!!")

