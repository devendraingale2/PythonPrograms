try:
    list=input("Enter Date(DD/MM/YY):").split("/")
    a=0
    for i in list:
        list[a]=int(list[a])
        a+=1
    
    if list[0]>31 or list[0]<0 or list[1]>12 or list[1]<0 or list[2]<0:
        print("Date Doesn't Exists..!!")
    else:
        print("Date IS Valid..")

except Exception:
    print("Enter Valid Date(DD/MM/YY)..!!")
