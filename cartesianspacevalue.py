import math as m
def cartesianvalues(theta,phi,radius):
    x=0
    y=0
    z=0
    x=radius*(m.sin(m.radians(theta)))*(m.cos(m.radians(phi)))
    y=radius*(m.sin(m.radians(theta)))*(m.sin(m.radians(phi)))
    z=radius*(m.cos(m.radians(theta)))

    print("X=",x)
    print("Y=",y)
    print("Z=",z)
    






theta=float(input("Enter Angle Theta:"))
phi=float(input("Enter Angle Phi:"))
radius=float(input("Enter Radius:"))
cartesianvalues(theta,phi,radius)
print()
