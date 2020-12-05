try:
    def evenreverse(size):
        for i in range(size,0,-1):
            if (i%2==0):
                print(i,end=" ")


    size=int(input("Enter Range:"))
    evenreverse(size)
    print()
except Exception:
    print("Enter Valid Integers..!!")
                                     
