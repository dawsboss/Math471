#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 08:31:10 2020

@author: grant : Math 471

2.1.4

"Write a computer code that takes a polynomial, defined by its
coefficients, and evaulates that polynomial and its first derivative
using Horner's rule. Test this code by applying it to each of the
polynomials in problem 1"

1)
(A) x^4 + 5x + 2
(B) x^6 + 2x^4 + 4x^2 + 1
(C) 5x^6 + x^5 + 3x^4 + 3x^3 + x^2 + 1
(D) x^2 + 5x + 6
"""
import math


# incvec - vector of polynomial coefficients
# val the x value you plug in
def HornersRule( incvec, val, verbose=True):
    n = len(incvec)
    p = incvec[n-1]
    
    for k in range(n-2, -1, -1):
        p = p*val + incvec[k]
    
    return (p)


#Gives a vector of coeficients if you derivived vect
def DeriveVec( vect ):
    n = len(vect)
    rtn = []
    for k in range(n):
        rtn.append(vect[k]*k)
    del rtn[0:1]#Gets rid of element that other wise would have been zeroed out x^0
    return rtn

polyvec = [ 1, 13, 2, 5, 1 ]
value = 1
results = HornersRule(polyvec, value)

print("Results: \n Poly{}\n x={}\n {}".format(polyvec, value, results))

test = DeriveVec(polyvec)
print(test)
dpoly = [ 13, 4, 15, 4 ]


