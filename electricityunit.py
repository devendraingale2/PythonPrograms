try:
    unit=float(input("Enter Electricity Charges In Units:"))

    if unit>0 and unit <51:
        print("Total Electricity Bill Is:",unit*0.50,"Rs.")
    if unit>50 and unit<151:    
        print("Total Electricity Bill Is:",unit*0.75,"Rs.")
    if unit>150 and unit<251:    
        print("Total Electricity Bill Is:",unit*1.20,"Rs.") 
    if unit>250:
        print("Total Electricity Bill Is:",unit*1.50,"Rs.") 
except ValueError:
    print("Invalid Units ..!!Please Enter Valid Unit Number..!!")

