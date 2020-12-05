f1i=open("input1.txt",'r')
f1o=open("DT.txt",'w')
f2o=open("DTLC.txt",'w')
f3o=open("MOP.txt",'w')
f4o=open("RT.txt",'w')
LC=0
line2=""
list=[]
RT=["AX","BX","CX","DX","AREG","BREG","A","B","C","D"]
MOP=["PRINT","READ","DS","DC","MOV","ADD","SUB","MUL","DIV","LOAD"]

for line in f1i.readlines():
	if line[0:5]=="START":
		str1=line.split(" ")
		for i in range(0,len(str1)):
			f1o.write(str1[i])
			f1o.write(" ")
			LC=int(str1[1])
	if line[0:5]=="START":
		f2o.write(line)
	else:
		LC+=1
		line3=""
		line2=line.split()
		line2.append(str(LC))
		for i in line2:
			line3+=" "+i
		f2o.write(line3.lstrip()+"\n")
	
	list=line.split(" ")
	print(list[0])
	for i in range(len(MOP)):
		if list[0]==MOP[i]:
			f3o.write(MOP[i]+" "+str(LC).lstrip()+"\n")
	for i in range(len(RT)):
		size=len(RT[i])	
		print(list[0])
		if list[1]=="AX":
			f4o.write("AX"+" "+str(LC).lstrip()+"\n")
			


















		

		
