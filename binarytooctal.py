try:
    num=input("Enter Binary Number:")
    dec=int(num,2)
    octal=oct(dec)
    print("Octal Number is:",octal)

except Exception:
    print("Enter Valid Integer.")
