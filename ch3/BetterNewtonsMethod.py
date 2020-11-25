#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:51:19 2020

@author: grant

Write a computer program that uses Newton's method to find the root
of a given function, and apply this program to find the root of 
the following functions, using xo as given. Stop the iteration 
when the error as estimated by |x n+ i — x n| is less than
10~ 6 . Compare to your results for bisection.

(g) - f(x) = x^2 - sin(x), x0 = 1/2
(h) - f(x) = x^3 - 2, x0 = 1
(i) - f(x) = x + tan(x), x0 = 3
(j) - f(x) = 2 - ln(x)/x, x0 = 1/3
"""


import math
import numpy as np
import matplotlib.pyplot as plt


def derivatice_approx( f, x, h ):
    return ( 8*f(x+h) - 8.0*f(x-h) - f( x + 2.0*h) + f(x - 2.0*h) ) / (12.0 * h)


def Better_Error_Newton_Method( f, x0, err, df=False, verbose = False):
    rtn = x0
    count = 0
    old = 0.0
    if(df):
        while(count<1000):
            count = count +1
            old = rtn    
            rtn = rtn - (f(rtn) / df(rtn))
            if(verbose):
                print(f"count: {count} | n: {n}\n rtn: {rtn}\n")
            
            if(abs(rtn-old) < err):
                break
            
    else:
        df = derivatice_approx
        while(count < 1000):
            count = count +1            
            old = rtn
            rtn = rtn - (f(rtn) / df(f, rtn, .000001))
            if(verbose):
                print(f"count: {count} | n: {n}\n rtn: {rtn}\n")
            
            if((abs(f(rtn))) + (abs(rtn-old)) < err):
                break
    
    return (rtn,count)




def Grapher_Newton_Method( f, x0, n, df=False, verbose = False):
    rtn = []
    rtn.append(x0)
    if(verbose):
        print(f"x0: {x0} | n: {n} | rtn: {rtn}\n")
    if(df):
        for i in range(0,n+1):
            rtn.append( rtn[i] - (f(rtn[i]) / df(rtn[i])) )
            if(verbose):
                print(f"i: {i} | n: {n}\n rtn: {rtn}\n")
    else:
        df = derivatice_approx
        for i in range(0,n+1):
            rtn.append( rtn[i] - (f(rtn[i]) / df(f, rtn[i], .000001)) )
            if(verbose):
                print(f"i: {i} | n: {n}\n rtn: {rtn}\n")  
    
    return rtn


def bist(f, a, b, eps, verbose = True):
    #compute some values that are reused often
    fa = f(a)
    fb = f(b)
    
    #check that we have a chance to succeed
    if(fa*fb < 0):#This means it crossed over the x axis
        n = int((math.log(b-a) - math.log(eps)) / math.log(2))+1
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
        return c,n
    
    else:
        print("No roots in interval")
        return False






FN = [
      lambda x: x**2 - math.sin(x),
      lambda x: x**3 - 2,
      lambda x: x + math.tan(x),
      lambda x: 2 - (np.log(x) / x)
     ]

xNot = [
        .5,
        1,
        3,
        1/3
       ]

names= [
        'x^2 - sin(x)',
        'x^3 - 2',
        'x + tan(x)',
        '2 - ln(x)/x'
       ]

err = 10**-6
n=0 # This will be used to store the number 
#       of itteration that was taken to find the root


#g | 0
name = names[0]
func = FN[0]
x0 = xNot[0]
result,n = Better_Error_Newton_Method(func, x0, err);
print(f"f(x) = {name} | n: {n} | X0: {x0} |\
 Root: x = {result}");

a=.5
b=3
result, n = bist(func, a, b, err, verbose=False);

print(f"BISECT: g(x) = {name} | n: {n} | [{a}, {b}] |\
 Root: fx = {result} | \
g(fx) = {FN[1](result)}\n");


#h | 1
name = names[1]
func = FN[1]
x0 = xNot[1]
result,n = Better_Error_Newton_Method(func, x0, err);
print(f"f(x) = {name} | n: {n} | X0: {x0} |\
 Root: x = {result}");
 
a=.5
b=3
result, n = bist(func, a, b, err, verbose=False);

print(f"BISECT: g(x) = {name} | n: {n} | [{a}, {b}] |\
 Root: fx = {result} | \
g(fx) = {FN[1](result)}\n");
 
 
 #i | 2
name = names[2]
func = FN[2]
x0 = xNot[2]
result,n = Better_Error_Newton_Method(func, x0, err);
print(f"f(x) = {name} | n: {n} | X0: {x0} |\
 Root: x = {result}");

a=2
b=3
result, n = bist(func, a, b, err, verbose=False);

print(f"BISECT: g(x) = {name} | n: {n} | [{a}, {b}] |\
 Root: fx = {result} | \
g(fx) = {FN[1](result)}\n");
 
 #j | 3
name = names[3]
func = FN[3]
x0 = xNot[3]
result,n = Better_Error_Newton_Method(func, x0, err);
print(f"f(x) = {name} | n: {n} | X0: {x0} |\
 Root: x = {result}");

a=.5
b=3
result = bist(func, a, b, err, verbose=False);

print(f"BISECT: g(x) = {name} | [{a}, {b}] |\
 Root: fx = {result}\n");