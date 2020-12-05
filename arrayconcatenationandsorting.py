import array as arr

lst=[]
lst2=[]
print("Enter First Array:")
for i in range(5):
    lst.append(input())
print("Enter Second Array:")
for i in range(5):
    lst2.append(input())

lst3=lst+lst2

print("Array After COncatenation:",lst3)
lst3.sort()
print("Array After Sorting:",lst3)
