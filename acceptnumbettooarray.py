import array as arr
lst=[]
num=input("Enter Number:")
for i in range(len(num)):
    lst.append(int(num[i]))
newarr=arr.array('i',lst)
for i in newarr:
    print(i,end=" ")
