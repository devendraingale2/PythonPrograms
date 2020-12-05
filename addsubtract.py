try:
    a,b=input("Enter Two Numbers in a Row:").split(" ")
    a=int(a)
    b=int(b)
    c=a+b;
    d=a-b;
    print("Addition Is:",c)
    print("Subtraction Is:",d)
except Exception as ve:
    print("Enter Valid Input..!!")
    print(ve)
    
