def prime(num):
    if int(num)>1:

        for i in range(2,int(num)):
            if int(num)%i==0:
                break
        else:
            print(int(num),end=" ")

num=input("Enter a Number:")
print("Prime Digits Are:",end=" ")
for i in range(len(num)):
    prime(num[i])

print()
