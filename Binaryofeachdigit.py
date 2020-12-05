'''
Program 2: Write a Program that prints Binary of Each Digit from entered
Number.
Input: 12
Output:
Binary of 1: 0001
Binary of 2: 0010
'''


num = int(input("Enter number : "))

def binPrint():
    global num
    while True:
        if(num == 0):
            break
        print(bin(num%10))
        num //= 10


binPrint()
