#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:06:03 2020

@author: grant


3. (50 pts.) For the function f(x) = arctan(x), write a program that 
estimates the (only) real root of f by computing 10 iterations of the 
bisection method (on the interval [-1,1]), as well as 10 iterations of
Newton’s method (with an initial value of x0 = 1).

Additionally, for Newton’s method, formulate an equation that must be 
satisfied by the value x = β, in order to have the Newton iteration 
cycle back and forth between β and −β. Run Newton’s Method
again for f (x) with 20 iterations and x 0 = β.
"""

import math

def derivatice_approx( f, x, h ):
    return ( 8*f(x+h) - 8.0*f(x-h) - f( x + 2.0*h) + f(x - 2.0*h) ) / (12.0 * h)


def bist(f, a, b, n, verbose = True):
    #compute some values that are reused often
    fa = f(a)
    fb = f(b)
    
    #check that we have a chance to succeed
    if(fa*fb < 0):#This means it crossed over the x axis
        for i in range(1, n+1):
            c = a + .5*(b-a)
            fc = f(c)
            if(verbose):
                print(f"a: {a} | b: {b} | c: {c} | fa: {fa} | fb: {fb} | fc: {fc}")
            
            if fa*fc < 0:
                b = c
                fb = fc
            elif fa*fc > 0:
                a = c
                fa = fc
            else:
                break
        return c
    
    else:
        print("No roots in interval")
        return False


def Newton_Method( f, x0, n, df=False, verbose = False):
    rtn = x0
    if(df):
        for i in range(0,n+1):
            rtn = rtn - (f(rtn) / df(rtn))
    else:
        df = derivatice_approx
        for i in range(0,n+1):
            rtn = rtn - (f(rtn) / df(f, rtn, .000001))
    return rtn


FN = [
      lambda x: math.atan(x),
      lambda x: 1/(1+x**2),
      lambda x: (2*x)-((1+x**2)*(math.atan(x)))#We pulled this from paper mathematics
     ]

xNot = [
        1
       ]

names= [
        'arctan(x)'
       ]

n = int(10)
a=-1
b=1

name = names[0]
func = FN[0]
x0 = xNot[0]


result = Newton_Method(func, x0, n);
print(f"f(x) = {name} | n: {n} | X0: {x0} |\
 Root: x = {result}");


result = bist(func, a, b, n, verbose=False);
print(f"BISECT: g(x) = {name} | n: {n} | [{a}, {b}] |\
 Root: fx = {result} | \
g(fx) = {FN[0](result)}\n");


print("---------------------")

#This first newton's method will solve for the x where the inf loop occurs
n=25
x0 = 1.3917952007 # what I got form the calc so I know it is close
func = FN[2]
result = Newton_Method(func, x0, n);
print(f"f(x) = {name} | n: {n} | X0: {x0} |\
 Root: x = {result}");


#This is the actual; problem but with x0 equal to beta found in previous newtons method
n=20
x0 = result
df = FN[1]
result = Newton_Method(func, x0, n, df=df);
print(f"f(x) = {name} | n: {n} | X0: {x0} |\
 Root: x = {result}");



