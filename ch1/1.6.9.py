#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:16:55 2020

@author: grant

Question 1.6.9

"Implement (as a computer program) the logarthim approximation
constructed in Problem 6. Compare it to the intrinsic logarithm 
function over the interval [.5, 1]. What is the maximum obeserved error?"

f(x) = ln(1-x / 1+x) = ln(1-x) - ln(1+x)
"""
import math
import matplotlib.pyplot as plt
import numpy as np

def approxLN(x0, x, N):
    sum = np.log(x0)
    for k in range(1,N+1):
        numerator = (float) (math.pow((x-x0),k) *  math.pow(-1,k+1))
        denominator = (float) (k * math.pow(x0, k))
        sum += (float) (numerator / denominator)
    return sum

xNot = .75
t = np.linspace(.5,1, num=200, endpoint=True)
N = 25



y = np.array([(approxLN(xNot, 1-x, N) - approxLN(xNot, 1+x, N)) for x in t])
#the array y is equal too an array of y values that are made from our approximating 
#   function. ln(1-x) - ln(1+x)
yReal = np.array([(np.log(1-x) - np.log(1+x)) for x in t])

plt.figure()
plt.plot(t, yReal, label='Real')
plt.plot(t,y,label='approx')
plt.legend()
plt.show()

errorY = np.array([abs((np.log(1-x) - np.log(1+x)) -\
(approxLN(xNot, 1-x, N) - approxLN(xNot, 1+x, N))) for x in t])

print("The max error is: ", max(errorY))

plt.figure()
plt.plot(t, errorY, label='Error')
plt.legend()
plt.show()


