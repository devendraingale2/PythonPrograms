import math as m
x1,y1=input("Enter (x1,y1):").split(",")
x2,y2=input("Enter (x2,y2):").split(",")
dist=m.sqrt((float(x2)-float(x1))**2+(float(y2)-float(y1))**2)
print("Total Distance Is:",dist,"units")

