try:
    def velocity(dist,time):
        vel=dist/time
        return vel
    
    dist=float(input("Enter Distance in meters:"))
    time=float(input("Enter Time in sec:"))
    vel=velocity(dist,time)
    print("The Velocity o Particle roaming in space is:",vel,"m/sec.")

except Exception:
    print("Enter Valid Inputs..")
