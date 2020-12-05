try:
    a,b=input("Enter Two Numbers in a Row:").split(" ")
    a=int(a)
    b=int(b)
    c=(a**3)+(b**3);
    d=(a**2)-(b**2);
    print("Addition of Cubes Of",a,"&",b," Is:",c)
    print("Subtraction Of Squares of",a,"&",b," Is:",d)
except Exception as ve:
    print("Enter Valid Input..!!")
    print(ve)

