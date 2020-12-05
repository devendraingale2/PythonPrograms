try:
    def add(r1,r2,i1,i2):
        real=r1+r2
        imag=i1+i2
        print("After Addition..")
        print("Complex Number is:",real,"+",imag,"i")

    print("Number 1.")
    real1=float(input("Real part1:"))
    imag1=float(input("Imaginary Part1:"))
    print("Number 2.")
    real2=float(input("Real part2:"))
    imag2=float(input("Imaginariy Part2:"))

    add(real1,real2,imag1,imag2)

except Exception as ve:
    print("Enter Valid Integers..!!\n",ve)
