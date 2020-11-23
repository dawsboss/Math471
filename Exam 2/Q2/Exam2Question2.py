#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:52:05 2020

@author: grant dawson

Question 2
"""
import math

def NaiveTrapezoid( a, b, n, f ):
    sum = .5*(f(a) + f(b))
    h = (b-a)/n
    for i in range(1,n):
        x = a + i*h
        sum = sum + f(x)
    return h*sum


def nn(a, b, h ):
    return int((b-a)/h)


def f1 ( x ):
    return ( (math.exp(x) - math.exp(-x)) / 2 )

def f2( x ):
    return ( math.pow( (1-math.pow(x,4)) , 1/2) )

def hh( a,b,n ):
    return (b-a)/n

a=0
b=1
x=2
h = []
for i in range(0, 7):
   h.append(1/x)
   x = x*2

for i in h:

    h=i
    result1 = NaiveTrapezoid(a, b, nn(a,b,h), f1)
    print(f"a={a} | b={b} | f(x)=(e^x - e^-x)/2 | n={nn(a,b,h)} | f'(x): {result1}")
    
    
    
    h=i
    result2 = NaiveTrapezoid(a, b, nn(a,b,h), f2)
    print(f"a={a} | b={b} | f(x)=sqrt(1-x^4) | n={nn(a,b,h)} | f'(x): {result2} \n")



