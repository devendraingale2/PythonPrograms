try:
    def area(len,breadth):
        area=len*breadth
        return area

    len=float(input("Enter Length:"))
    breadth=float(input("Enter Breadth:"))
    print("Area of Rectangle is:",area(len,breadth))

except Exception:
    print("Enter Valid Numbers..!!")
