import array as arr
lst=[]
num=input("Enter Number:")
a=num[::-1]
for i in range(len(a)):
    lst.append(int(a[i]))
newarr=arr.array('i',lst)
for i in newarr:
    print(i,end=" ")
