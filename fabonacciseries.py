
def fabonacci(size):
    a=1
    b=0
    c=a+b
    print("Fabonacci Series Upto",size,":",end=" ")
    for i in range(size):
        c=a+b
        print(c,end=" ")
        a=b
        b=c


size=int(input("Enter Maxima:"))
fabonacci(size)
print()
