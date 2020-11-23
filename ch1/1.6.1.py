#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 08:24:08 2020

@author: grant

Ex 1.6
"For each value in the previous porblem, compute the logarithm
approximation using degree 4 polynomial from (1.12). 
What is the rror compared to the logarithm on your calculator?"

1.6.1

"Write each of the following in the form x = f / times 2^Beta
for some f in [1/2 , 1]."

    (a) x = 13;
    (b) x = 25;
    (c) x = 1/2;
    (d) x = 1/10;
"""

import math

#Create a function to find and return f and \Beta, as 
#   representations for some f in [1/2, 1] of form
#   x = f \times 2^\Beta:
#Assumes x is positive
def createRep( x ):
    x = float(x)
    x = abs(x)
    Beta = 0
    f = 0.0
    
    while( x>1.0 ):
        x = x/2.0
        Beta = Beta+1
    
    return(x, Beta)
    
val = 13
f, Beta = createRep( val )
print("The rep. for val = {} is: {} times 2^{}"\
      .format(val, f, Beta))
    
