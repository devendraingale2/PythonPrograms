try:
    def divisor(num):
        for i in range(1,(int(num))+1):
            if int(num)%i==0:
                set1.add(i)


    set1=set()
    a=input("Enter Number:")
    for i in range(len(a)):
        divisor(a[i])

    print("Perfect Divisors Are:",set1)
except Exception:
    print("Enter Valid Integer..!!")
