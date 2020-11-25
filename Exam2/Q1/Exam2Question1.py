#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 08:04:10 2020

@author: grant dawson

Question 1

"""

import math
import numpy as np



def D2h( f, x, h ):
    return ( (f(x+h) - f(x-h)) / (2.0*h) )

def tri(f, x, h):
    return ( ((4*D2h(f,x,h)) - D2h(f,x,2.0*h)) / 3.0 )





def gx( x ):
    return( -1.0 * math.log(math.cos(x)) )

def fx( x ):
    return( math.pow(x, math.pow(x,x)) )

f = fx
g = gx
j = 4
x=1
h = []
for i in range(0, 4):
   h.append(1/j)
   j = j*2

for i in h:
    result = tri(f, x, i)
    
    print(f"f(x) || x: {x} | h: {i} | result: {result}")


    result = tri(g, x, i)
    
    print(f"g(x) || x: {x} | h: {i} | result: {result}")

    