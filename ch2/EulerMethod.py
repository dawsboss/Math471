#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 08:32:22 2020

@author: grant
Euler's Mathod for IVP
2.3
"""
import math
import numpy as np
import matplotlib.pyplot as plt

#Import other py files
#import library.ch2lib as ch2

#ch2.printme()

#Have F' trying to find f

#########
#
#Approximates solutions to first order Ordinary Diferencial Equation(ODE)
#
#   f function
#   t provided numpy array
#   y0 init point
#   h step size
#   a start to interval
#   b end to interval
#
def EulersMethod( f, t, y0, h, a, b, verbose=False ):
    rtn = np.arange( a, b+h, h)
    rtn[0] = y0
    
    
    for i in range(1, len(t)):
        rtn[i] = rtn[i-1] + h * f ( t[i-1], rtn[i-1])
        if verbose:
            print("step: {:4} | t: {: 8.8f} | y: {: 10.10f}"\
                  .format(i, t[i], rtn[i]))
                
        
    
    return rtn
    
#Create ODE from class
def ode(t, y):
    return(y * (1.0 - 2.0*t))

#Actual solution to ODE
def exact_solution(t):
    return(math.exp(t-t**2.0))

#Initial value (t = ?)
y0 = 1.0

#Interval
a = 0.0
b = 3.0

#how many subintervals do we want for [a,b]?
hinv = 3
h = (b-a)/hinv

#Domain space
t = np.linspace(a, b, num=hinv+1, endpoint=True)


approx = EulersMethod( ode, t, y0, h, a, b, verbose=True)
print("Result: {}".format(approx))

print()
print(t)

#Reference data
real = np.array( [exact_solution(x) for x in t] )


plt.figure(figsize=(8,6))
plt.plot(t,approx, label="naive with h={}".format(h))
#plt.plot(t,better, label="better with h={}".format(h))
plt.plot(t,real, label="real")
plt.legend()

