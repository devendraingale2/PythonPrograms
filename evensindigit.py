num=input("Enter Number:").split()
count=0
for i in range(len(num[0])):
    if int(num[0][i])%2==0:
        count+=1

print("There are",count,"even digits in",num)
