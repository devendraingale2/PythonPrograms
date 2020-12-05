

dict1 = dict(input("Enter key and value : ").split() for i in range(int(input("Enter range : "))))

print(dict1)
str1 = ""
for a in dict1:
    for b in dict1:
        if(a == dict1[b]):
            str1 = a
            break
dict1.pop(str1)
print(dict1)

