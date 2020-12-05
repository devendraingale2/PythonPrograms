sum=0
num=input("Enter Number:")
print(num)

for i in range(len(num)):
    sum+=int(num[i])

print("Sum:",sum)
aver=round(sum/len(num))
print("The Average If Digits is:",aver)

