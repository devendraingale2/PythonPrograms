import math as m
x1,y1=input("Enter (x1,y1):").split(",")
x2,y2=input("Enter (x2,y2):").split(",")
x3,y3=input("Enter (x3,y3):").split(",")
distAB=m.sqrt((float(x2)-float(x1))**2+(float(y2)-float(y1))**2)
distAC=m.sqrt((float(x3)-float(x1))**2+(float(y3)-float(y1))**2)
distBC=m.sqrt((float(x3)-float(x2))**2+(float(y3)-float(y2))**2)
print("Distance of AB:",distAB,"units")
print("Distance of BC:",distBC,"units")
print("Distance of AC:",distAC,"units")

peri=distAB+distBC+distAC
print("Perimeter of Triangle:",peri)
