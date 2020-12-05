try:
    def deficient(num):
        div=0
        for i in range(1,num):
            if num%i==0:
                div=div+i

        if div<num:
            print(num,"is Deficient as",div,"<",num)
        elif div>num:
            print(num,"is Abundant as",div,">",num)

    num=int(input("Enter Number:"))
    deficient(num)
    print()

except Exception:
    print("Enter Valid Integer..!!")

