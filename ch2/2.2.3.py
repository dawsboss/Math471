#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 08:04:10 2020

@author: grant

Problem 2.2.3

"Write a computer program that uses the same derivative approximation as in
the previos problem to approximate the first derivative at x = 1 for each of 
the following functions, usiung h^(-1) = 4,8,16,32. Verify that the predicted 
theoreticazl accuracy is obtained - in other words, show that your results 
are consistent with the analysis in this section."

(a) f(x) = sqrt(x+1)
(b)
(c)
(d)
(e) f(x) = ln(x)
"""

import math
import numpy as np
import matplotlib.pyplot as plt

#f: approximated function
#x: value we are determining the derivative
#h:infintesimal offset for approximation
#
#returns: derivative of f(x) at x  
def naive_derivatice_approx( f, x, h ):
    rtn = 0.0
    
    rtn = ( f(x+h) - f(x) )/h

    #print(rtn)
    return(rtn)

#
def better_derivatice_approx( f, x, h ):
    rtn = 0.0
    
    rtn = ( f(x+h) - f(x-h) )/(h*2)

    #print(rtn)
    return(rtn)




def sinpi( x ):
    return( math.sin( math.pi * x ) )

def Dsinpi ( x ):
    return( math.pi * math.cos( math.pi * x ) )


val = math.pi / 2
h = .1
#approx f(x)
f = sinpi
#real f(x)
rF = Dsinpi

result = naive_derivatice_approx(f, val, h)

print("{} function with derivative evaluated at {}, with h={}"\
      .format(f.__name__, val, h))

#naive approx
print("\thas result = {}".format(result))

#Real answer
refresult = rF(val)
print("\tReference result = {}".format(refresult))

#better apprimating of derivative
betterResult = better_derivatice_approx(f, val, h)
print("\thas better result = {}".format(betterResult))

##Ploting

#Establsih domain
t = np.linspace(0, 2, num=100, endpoint=True)

#List comprehention
naive = [ naive_derivatice_approx(f, x, h) for x in t]
better = [ better_derivatice_approx(f, x, h) for x in t]
real = [ rF(x) for x in t]


plt.figure(figsize=(8,6))
plt.plot(t,naive, label="naive with h={}".format(h))
plt.plot(t,better, label="better with h={}".format(h))
plt.plot(t,real, label="real")
plt.legend()


