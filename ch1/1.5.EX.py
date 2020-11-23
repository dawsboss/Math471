#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:14:08 2020

@author: grant


We investigate representing the following function as a 
    Taylor Series (and polynomials):

  f(x) = { e^(-x^-2) if x neq 0; 0 if x=0 }
  
  Part A. Create dregree 2 approximation of f, centered at 1(later at )

  Part B. Plot f and approximation function
  
  Part C. Change center of approximation to 1/2; plot all
  
  part D. Play (centers, plot ranges)
  
  part E. Rsearch: Does the error in approximation improve much for
      higher degreecapproximations on [0,2]?
      Why or why not?


"""
import math
import numpy as np
import matplotlib.pyplot as plt


def f( x ):
    
    rtn = 0.0
    
    if(x!=0):
        rtn = math.exp( -1/(x**2.0) )
    
    return rtn


#Lambda dunction for the degree 2 poly approximation for f(x)
approx = lambda x: math.exp(-1.0) * (1.0 + 2.0*(1 - 1.0)**2.0)
    





vals = [0,1,2]




for x in vals:
    print("x={}, f(x)={:12.10f}, p2(x)={:12.10f} "\
          .format(x, f(x), approx(x)))



#Plottig below

#Created the domain space
t = np.linspace(0,2, num=100, endpoint=True)

#Create range for our plot
y = np.array([f(x) for x in t])


#Plot what we have made
plt.plot(t,y,label='f(x)')
plt.legend()
plt.show()









