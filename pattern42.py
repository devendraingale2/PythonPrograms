for outer in range(1,5):
    for inner in range(1,5):
        if(inner == outer):
            print("=",end=" ")
        else:
            print(inner,end=" ")
    print()
