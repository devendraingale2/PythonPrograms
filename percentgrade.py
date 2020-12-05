try:
    print("Enter Marks For Subjects Below.")
    phy=float(input("Physics:"))
    chem=float(input("Chemistry:"))
    bio=float(input("Biology:"))
    math=float(input("Mathematics:"))
    comp=float(input("Computer:"))
    if(phy<0 or chem<0 or bio<0 or math<0 or comp<0):
        raise Exception


    perc=float((phy+chem+bio+math+comp)/500)*100

    if perc>=90 and perc<=100:
        print("Total Percentage:",perc,"% :Grade A")
    elif perc>=80 and perc <90:
        print("Total Percentage:",perc,"% :Grade B")
    elif perc>=70 and perc <80:
        print("Total Percentage:",perc,"% :Grade C")
    elif perc>=60 and perc <70:
        print("Total Percentage:",perc,"% :Grade D")
    elif perc>=40 and perc <60:
        print("Total Percentage:",perc,"% :Grade E")
    elif perc<40:
        print("Total Percentage:",perc,"% :Grade F")
    elif perc>100 or perc<=0:
        raise Exception
except Exception as ve:
    print("ValueError:Insert proper marks..!!",ve)

