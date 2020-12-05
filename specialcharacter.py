a=input("Input:")
b=ord(a)

if (b>=65 and b<=90) or (b>=97 and b<=122):
    print(a,"is an Alplabet.")
elif (b>=48 and b<=57):
    print(a,"is a Numeric Digit.")
else:
    print(a,"Is a Special Character.")
