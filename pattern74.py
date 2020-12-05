'''
A0 B1 C2 D3 E4 F5 G6
  H2 I4 J6 K8 L10
    M4 N6 O8
      P8
'''
A=65
a=0
b=2
c=0
d=0
for i in range(4):
    for space in range(i):
        print("  ",end="")
    for j in range(c+i,7-i):
        print(chr(A)+str(a),end=" ")
        a+=1
        A+=1 
    
    d+=b
    a=d
    print()
