def slope(A,B,C,D):
    return (float)(float(D)-float(B))/(float(C)-float(A))


A,B=input("Point A,B:").split(",")
C,D=input("Point C,D:").split(",")
print("Slope Of Line Is:",slope(A,B,C,D))
print()
