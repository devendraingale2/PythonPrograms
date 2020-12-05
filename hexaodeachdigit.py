
def hexdigit(num):
    hexa=hex(int(num))
    print("Hex of",num,"is:",hexa)
        

num=input("Enter Number:")
for i in range(len(num)):
    hexdigit(num[i])
