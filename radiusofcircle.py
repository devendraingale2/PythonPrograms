import math as m
def radiusofcircle(area):
    radius=m.sqrt(area/m.pi)
    print("Radius of circle is:",radius)

area=float(input("Enter Area:"))
radiusofcircle(area)
print()
