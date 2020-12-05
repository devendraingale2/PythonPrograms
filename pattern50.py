'''
      *
    # *
  # * *
# * * *
'''

a="#"
b="*"
for i in range(1,5):
    for space in range(5-i):
        print(" ",end="\t")
    print(a,end="\t")
    for j in range(i-1):
        print(b,end="\t")
    print()
