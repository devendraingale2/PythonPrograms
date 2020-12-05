def deficient(num):
    deficient=[]
    abundant=[]
    for k in range(1,num+1):
        sum=0
        for i in range(1,k):
            if k%i==0:
                sum+=i
        if sum<k:
            deficient.append(k)
        else:
            abundant.append(k)
    print("Deficient Numbers upto",num,":",deficient)
    print("Abundant Numbers upto",num,":",abundant)




num=int(input("Enter Range:"))
deficient(num)
