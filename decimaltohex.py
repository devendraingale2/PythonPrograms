try:
    def hexal(num):
        hexa=hex(num)
        print("Hexadecimal Is:",hexa)

    
    num=int(input("Enter Decimal Number:"))
    hexal(num)
except Exception:
    print("Enter Valid Integer..!!")
