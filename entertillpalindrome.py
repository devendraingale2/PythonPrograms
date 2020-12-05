def palindrome(start):
    if start==start[::-1]:
        print("Terminating..")
        flag=0
        exit()


flag=1
while(flag==1):
    num=input("Enter Number:")
    palindrome(num)
