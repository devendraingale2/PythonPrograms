def pattern19(CH,ch,size):
    for i in range(1,size+1):
        for j in range(i):
            if i%2==0:
                print(CH,end=" ")
            if i%2!=0:
                print(ch,end=" ")
        print()


size=int(input("Enter Size:"))
CH=input("Enter Capital Character:")
ordin=ord(CH)+32
ch=chr(ordin)
pattern19(CH,ch,size)
    

