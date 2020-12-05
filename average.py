
n=int(input("Enter How Many Numbers:"))
print("Enter Numbers:",end=" ")
sum=0
avg=0
for i in range(n):
    a=int(input())
    sum+=a

print("Average is:",sum/n)
