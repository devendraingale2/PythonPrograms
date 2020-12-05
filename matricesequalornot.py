def areSame(A,B): 
      
    for i in range(N): 
        for j in range(N): 
            if (A[i][j] != B[i][j]): 
                return 0
    return 1
  

A= [ [1, 1, 1, 1], 
    [2, 2, 2, 2], 
    [3, 3, 3, 3], 
    [4, 4, 4, 4]] 
   
B= [ [1, 1, 1, 1], 
    [2, 2, 2, 2], 
    [3, 3, 3, 3], 
    [4, 4, 4, 4]] 
N=4                      
if (areSame(A, B)==1): 
    print("Matrices are identical") 
else: 
    print("Matrices are not identical") 
