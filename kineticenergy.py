try:
    def KEenergy(mass,vel):
        ke=0.5*mass*vel**2
        print("The Kinetic Energy Is:",ke,"Joules")

    mass=float(input("Enter Mass in Kg:"))
    vel=float(input("Enter Velocity in m/sec:"))
    KEenergy(mass,vel)

except Exception as ve:
    print("Eter Valid Integers..!!\n",ve)

