try:
    a,b=input("Enter Dividend & Divisor:").split(" ")
    b=float(b)
    a=float(a)
    c=a/b
    print("Quotient Is:",c)
    if b==0:
        raise ZeroDivisionError
except ZeroDivisionError:
    print("Infinity.(Cant Divide By Zero.)")


