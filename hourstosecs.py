try:
    def seconds(hours):
        sec=hours*60
        print(hours,"hours=",sec,"seconds.")


    hours=float(input("Enter Hours:"))
    seconds(hours)
    print()

except Exception:
    print("Enter Valid Integers..!!")
