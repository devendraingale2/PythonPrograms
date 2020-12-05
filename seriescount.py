num=int(input("Enter Range:"))
sum=0
for i in range(1,num+1):
    sum+=i**i
print("Actual Product:",sum)
sum=str(sum)
count=len(sum)
print("\nLast 10 Digits of Product:",sum[count-10:count])

