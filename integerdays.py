a=int(input("Input:"))

try:
    if a==1:
        print("Monday.")
    elif a==2:
        print("Tuesday.")
    elif a==3:
        print("Wednesday.")
    elif a==4:
        print("Thursday.")
    elif a==5:
        print("Friday.")
    elif a==6:
        print("Saturday.")
    elif a==7:
        print("Sunday.")
    elif b not in range(1,8):
        raise Exception

except Exception:
    print("Not a Valid Week Integer..!!")
