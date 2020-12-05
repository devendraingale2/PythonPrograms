try:
    a=int(input("Enter Number A:"))
    b=int(input("Enter Number B:"))
    c=input("Enter Operation Symbol(+,-,*,/,%):")
            
    if c=='+':
        print("Addition Of",a,"&",b,"is:",a+b)
    if c=='-':
        print("Subtraction Of",a,"&",b,"is:",a-b)
    if c=='*':
        print("Multiplication Of",a,"&",b,"is:",a*b)
    if c=='/':
        print("Division Of",a,"&",b,"is:",a/b)
    if c=='%':
        print("Modulus Of",a,"&",b,"is:",a%b)
except Exception as ve:
    print("Enter Valid Inputs..!!")
    print(ve)

