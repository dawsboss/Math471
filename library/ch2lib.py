#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 08:36:24 2020

@author: grant
"""
import math
import numpy as np
import matplotlib.pyplot as plt


def printme():
    print("Hi there, friend!")

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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    