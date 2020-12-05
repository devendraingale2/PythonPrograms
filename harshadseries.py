a=input("Enter Number:")
lst=[]
for x in range(2,int(a)):
	if(int(a)%x==0):
		lst.append(x)
i=0		
for y in a:
	i=i+int(y)
j=0	
for z in lst:
	if(z==i):
		j=j+1
if(j==0):		
	print(a,"is not harshad Number")
else:
	print(a,"is harshad Number") 	
