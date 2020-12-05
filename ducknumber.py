num=input("Enter Number:")
lst=[]
for i in range(len(num)):
    lst.append(num[i])
first=int(lst[0])

if lst.__contains__('0')==True:
    if first!=0:
        print(num,"is a Duck Number.")
    else:
        print(num,"is not a Duck Number.")

else:
    print("It is Not Duck Number.")
