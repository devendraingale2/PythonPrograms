'''
Program 5: Write a Program that takes a number as input from user and prints
Quotient of division of each digit from that number with the number itself.
Input: 124
Output:
The Quotients of Divisions are;
124/1 = 124
124/ 2 = 62
124/4 = 31
'''



num = int(input("Enter number : "))
print("Quotients of Divisions are;")
for i in str(num):
    print(num,"/",i," = ",num/int(i))
