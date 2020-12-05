try:
    a=[]
    n=int(input("How Many Numbers?:"))
    print("Enter Numbers:")
    for i in range(0,n):
        inputs=int(input())
        if inputs<0:
            print("Oops Negative Numbers Are Not Alowed..!!")
            break
        else:
            a.append(inputs)
    print(a)
    print()
except Exception:
    print("Eter Valid Integer..!!")
