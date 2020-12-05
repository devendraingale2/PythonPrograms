num=input("Enter Number:")
digits=[]
sum=0
ave=0
for i in range(len(num)):
    digits.append(int(num[i]))
    sum+=digits[i]

print("Sum Is:",sum)
ave=sum/len(num)
print("Average Is:",ave)
