
def primeno(x):
    if int(x)>0:

        for i in range(2,int(x)):
            if (int(x)%i)==0:
                break
        else:
            print(int(x),end=" ")


        
x=input("Enter Number:")
print("Prime Digits Are:",end=" ")
for i in range(len(x)):
    primeno(x[i])

print()
