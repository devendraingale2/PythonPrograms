A=65
flag=1
lst=[]
while flag==1:
    ch=input("Enter Alphabet:")
    if ord(ch)==A:
        lst.append(ch)
        print(lst)
        A+=1
    else:
        print("Incorrect Order..")
        flag=0
