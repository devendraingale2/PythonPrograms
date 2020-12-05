try:
    rad=float(input("Enter the Radius:"))
    pi=22/7
    print("Area of circle is:",pi*rad*rad)
except ValueError:
    print("Improper Radius..!!")
