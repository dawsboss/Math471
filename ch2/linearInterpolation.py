# Justin Ventura
# MATH471

"""
Linear Interpolation.

2.4
"""

import math
import numpy as np

# From pg 67 section 2.4 #3 and theorem 2.1
def error(fvals, xval, x, h):
    left = (fvals[x-1] - 2*fvals[x] + fvals[x+1])/(h**2)
    right = (fvals[x] - 2*fvals[x+1] + fvals[x+2])/(h**2)
    use = 0
    if(left > right):
        use = left
    else:
        use = right  
    return (1/8 *(h)**2 * use)
    

# NOTE: This function requires the matrix.
def linear_interpolation(F, x):
    interpolation = 0.0

    # Rows never needed.
    rows, cols = F.shape

    if F[0, 0] < x < F[0, cols-1]:
        i = 0
        while x > F[0, i]:
            i += 1    
        interpolation = (F[1, i] - F[1, i-1]) / (F[0, i] - F[0, i-1]) * \
(x - F[0, i-1]) + F[1, i-1]
    elif x == F[0, 0]:
        interpolation = F[0, 0]
    elif x == F[0, cols-1]:
        interpolation = F[0, cols-1]
    else:
        print('invalid')

    return interpolation


xVals = np.array([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0])
gvals = np.array([1.0, .9513507699, .9181687424, 
                    .8974706963, .8872638175,
                    .8862269255, .8935153493, 
                    .9086387329, .9313837710, 
                    .9617658319, 1.0])


# Make the table of values.
F = np.matrix([[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0],
                   [1.0, .9513507699, .9181687424, 
                    .8974706963, .8872638175,
                    .8862269255, .8935153493, 
                    .9086387329, .9313837710, 
                    .9617658319, 1.0]])



# Problem x-values.
Xs = [1.930, 1.29, 1.005, 1.635]

# Corresponding values.
bounds = [2, 5, 4, 3, 7]

# Resulting values from linear interpolation.
results = [linear_interpolation(F, x) for x in Xs]
errResults = [error(gvals, xVals, x, xVals[1]-xVals[0]) for x in bounds]

for i in range(len(Xs)):
    print('Gamma({}) = {}'.format(Xs[i], results[i]))
    #print('\tmax error: {}'.format(error_bound(bounds[i])))
for i in range(len(errResults)):
    print(f"error {errResults[i]}")