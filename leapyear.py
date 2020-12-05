try:
    year=int(input("Enter Year:"))
    if year%4==0:
        print("The Year you entered is a Leap Year.")
    else:
        print("The Year you entered is not a Leap Year.")
except ValueError as ve:
    print("ValueError:",ve)
