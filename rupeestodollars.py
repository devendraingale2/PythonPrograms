try:

    def dollar(rupee):
        dollr=rupee*0.014
        print("Equivlent Dollars=",dollr,"$")

    rupee=float(input("Enter Rupees:"))
    dollar(rupee)

except Exceptions as ve:
    print("Enter Valid Integers..\n",ve)
