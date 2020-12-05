start=int(input("Enter Start No:"))
end=int(input("Enter Ending No:"))
lst=[]
for i in range(start,end+1):
    if (i*i)%10==i:
        lst.append(i)
    
print("Automorphic between",start,"and",end,"are:",lst)

