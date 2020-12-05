def Abundant(num):
    div=0
    for i in range(1,int(num/2)+1):
        if num%i==0:
            div+=i

    if div>num:
        print(num,end=" ")
    




num=int(input("Enter Limit number:"))
print("Abandant Numbers between 1 &",num,"are:",end=" ")
for i in range(1,num+1):
    Abundant(i)
print()
