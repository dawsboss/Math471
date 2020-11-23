"""

Chapter 2.6.5 and 2.6.7

"""

# Numpy
import numpy as np

#Finds the solution to a tridiagonal system Ax = b.
#A (numpy.matrix): This will be the coefficient matrix A.
#b 
#verbose (bool, optional): True debugging/logging. Defaults to False.

def tridiagonal(A, inF): 
    # Dimensions
    rows, cols = A.shape

    # making f vector from inF
    f = inF.copy()

    # Creating a new matrix that it wont be bad to edit
    d = np.diagonal(A).copy()
    up = np.diagonal(A, 1).copy()
    low = np.diagonal(A, -1).copy()

    # Elimination phase:
    for i in range(1, rows):
        d[i] -= up[i-1]*low[i-1]/d[i-1]
        f[i] -= f[i-1]*low[i-1]/d[i-1]

    # Backsolving phase:
    f[-1] = f[-1]/d[-1]
    for i in range(rows-2, -1, -1):
        f[i] = (f[i] - up[i]*f[i+1])/d[i]

    return f



A = np.matrix([[1.0, 1/2, 0.0, 0.0],
               [1/2, 1/3, 1/4, 0.0],
               [0.0, 1/4, 1/5, 1/6],
               [0.0, 0.0, 1/6, 1/7]])

b = np.matrix([[2.0],
              [23/12],
              [53/30],
              [15/14]])

print('2.6 Algorithm:')
print(tridiagonal(A, b))
print('Numpy solution:')
print(np.linalg.solve(A, b))