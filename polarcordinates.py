import math
def polarcordinate(angle,radius):
    x=0
    y=0
    x=radius*(math.cos(math.radians(angle)))
    y=radius*(math.sin(math.radians(angle)))
    print("X is:",x)
    print("Y is:",y)


angle=float(input("Enter Angle:"))
radius=float(input("Enter Radius:"))
polarcordinate(angle,radius)
print()
