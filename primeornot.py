try:
    def primeno(x):
        if x>1:

            for i in range(2,x):
                if (x%i)==0:
                    print(x,"is not Prime.")
                    break
            else:
                print(x,"is Prime.")

        else:
            print(x,"is not Prime.")
    x=int(input("Enter Number:"))
    primeno(x)
    print()
except Exception:
    print("Enter Valid Integers..!!")
