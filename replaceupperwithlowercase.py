string=input("Enter String:")
newstring=''
for i in string:
    if (i.isupper())==True:
        newstring+=(i.lower())
    elif (i.islower())==True:
        newstring+=(i.upper())
    elif (i.isspace())==True:
        newstring+=i

print("String before Conversion:",string)
print("String After Conversion:",newstring)
