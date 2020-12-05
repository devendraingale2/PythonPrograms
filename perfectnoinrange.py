try:
    def Perfect(start, end):
        for i in range(start, end + 1):
            sum1 = 0
            for x in range(1, i):
                if(i % x == 0):
                    sum1 = sum1 + x
            if (sum1 == i):
                print(i)
    
    size=int(input("Enter Range:")) 
    Perfect(1, size)
except Exception as ve:
    print("Enter Valid Integer..!!")
    print(ve)

