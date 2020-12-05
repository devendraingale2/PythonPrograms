try:
    def Perfect(start, end):
        list=[]
        for i in range(start, end + 1):
            sum1 = 0
            for x in range(1, i):
                if(i % x == 0):
                    sum1 = sum1 + x
            if (sum1 == i):
                list.append(sum1)
        for i in range(1,end+1):
            if (i==list[0]) or (i==list[1]):
                continue
            else:
                print(i,end=" ")
    size=int(input("Enter Range:")) 
    Perfect(1, size)
except Exception as ve:
    print("Enter Valid Integer..!!")
    print(ve)


