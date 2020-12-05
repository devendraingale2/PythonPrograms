per=6
count=0
num=input("Enter Number:")
for i in range(len(num)):
    if int(num[i])==per:
        print(num,"contains",per,"which is perfect number.")
        count+=1
if count==0:
    print(num,"contains no any digit having perfect number.")
