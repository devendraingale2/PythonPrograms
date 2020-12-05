try:

    def fibonacci(num):
        a=1
        b=0
        c=0
        print("Fibonaci Series Upto",num,"is:",end="")
        for i in range(1,num+1):
            c=a+b
            print(c,end=" ")
            a=b
            b=c



    num=int(input("Enter Number:"))
    fibonacci(num)
    print()
except Exception:
    print("Enter Valid Integers..!!")
