try:
    def meters(kms):
        return kms*1000

    kms=float(input("Enter Kilometers:"))
    print(kms,"kms is equal to",meters(kms),"meters.")

except Exception:
    print("Enter Valid Integers,,!!")
