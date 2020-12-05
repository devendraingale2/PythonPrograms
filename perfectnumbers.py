try:

    def Perfect(num1):
        sum1 = 0
        for i in range(1,num1):
            if(num1 % i == 0):
                sum1 = sum1 + i
        return sum1


    num1 = int(input("Please Enter any number: "))
    if (num1 == Perfect(num1)):
        print("%d is a Perfect Number"%num1)
    else:
        print("%d is not a Perfect Number"%num1)
except Exception as ve:
    print("Enter Valid Integer..!!")
    print(ve)

