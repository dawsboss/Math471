# Justin Ventura MATH471
# Secant Method

"""
Chapter 3.8.2: Perform 3 steps of the secant method to the function
f(x) = x^3 - 2 using x_0 = 1, x_1 = 0.

(compare that to x_0 = 0, x_1 = 1)
"""

import math

# Secand Method function:
#x_0: First initial guess.
#x_1: Second term after.
#f: This is the function being evaluated in terms of x.
#err: Error tolerance.
#verbose: For logging. Defaults to False.
def secant_method(x0, x1, f, err, verbose):
    if verbose:
        print(f'x0={x0} x1={x1}')

    i = 1
    limit = 500

    f0 = f(x0)
    f1 = f(x1)

    while abs(x1 - x0) > err and i < limit:
        root = x1 - f1 * (x1 - x0)/(f1 - f0)
        f_x = f(root)
        x0 = x1
        x1 = root
        f0 = f1
        f1 = f_x
        
        if verbose:
            print(f'i: {i} root: {root}')

        # If we are converging, then stop.
        if abs(x1 - x0) < err:
            root = x1
            break

        i += 1

    return root  # Return the estimated root within err tolerance.


functions = [lambda x: math.pow(x, 3) - 2]
x0 = 1
x1 = 0
print('Question 1 result for reference:')
secant_method(x1, x0, functions[0], 1e-10, True)
print('Question 2 result:')
secant_method(x0, x1, functions[0], 1e-10, True)