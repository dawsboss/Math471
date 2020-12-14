"""
Chapter 3.4: Newton's Method for division.

3.4.5: Compute 1/0.75 = 1.333 and 1/(2/3) = 1.5 with the x_0 as
       suggested from the text.

NOTE: The polynomials defined below I played around with, but I will
not present because other students may be presenting them as the polys
are called for in other homework questions.
"""

import numpy as np

# Newtons method for fast division.
#a:          the a in 1/a.
#err:        The error tolerance.
#x0:         A function for the initial guess.


def Newton_Divide(a, err, x0=False, verbose=False):
    if not x0:
        x0 = 3.0 - 2.0 * a 

    prev = x0 * (2.0 - a * x0)
    rtn = prev * (2.0 - a * prev)

    if verbose:
        print(f'Iteration {1}: {prev}')
        print(f'Iteration {2}: {rtn}')

    i = 3
    limit = 500

    # Divergence and max for itter 
    while  np.abs(rtn - prev) > err and i < limit:
        prev = rtn
        rtn = prev * (2.0 - a * prev)
        if verbose:
            print(f'Iteration {i}: {rtn}')
        i += 1

    return rtn  # Return the result.



print(f'Compute 1/0.75 = 1.333 [with tolerance {10**-6}]')
print(Newton_Divide(0.75, 10**-6, verbose=True))

print(f'\nCompute 1/(2/3)) = 1.5 [with tolerance {10**-6}]')
print(Newton_Divide(2/3, 10**-6, verbose=True))