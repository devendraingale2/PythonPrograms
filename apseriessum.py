'''
Program 1: Write a Program that prints Sum an Arithmetic Progression (A.P.)
series. Take Starting element, Total count of elements in A.P. & the Common
Difference from user.
Input:
Starting Element: 1
Number of Elements: 8
Common Difference: 5
Output: The AP is: 1 + 6 + 11 + 16 + 21 + 26 + 31 + 36 = 148
'''



start = int(input("Starting Element : "))
num = int(input("Number of Elements : "))
diff = int(input("Common Difference : "))

sum = 0
for i in range(start,(start+num*diff),diff):
    print(i,end=" ")
    sum += i
print("\nSum : ",sum)
