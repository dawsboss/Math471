#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 08:28:02 2020

@author: grant

Find roots using Newton's Method

2. (50 pts.) Consider the function f (x) = x/2 − sin(x). Code Newton’s Method in Python to show that f
has a root on the interval [1,3]. Also, write Python code which uses the Newton error estimate formula
to help you to determine how close x 0 has to be to the root to guarantee convergence.
"""
import math

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
                print(f"count: {count} | rtn: {rtn}\n")
            
            if(abs(rtn-old) < err):
                break
            
    else:
        df = derivatice_approx
        while(count < 1000):
            count = count +1            
            old = rtn
            rtn = rtn - (f(rtn) / df(f, rtn, .000001))
            if(verbose):
                print(f"count: {count} | rtn: {rtn}\n")
            
            if((abs(f(rtn))) + (abs(rtn-old)) < err/5):
                break
    
    return (rtn,count)


FN = [
      lambda x: (x/2) - math.sin(x)
     ]


names= [
        'x^2 - sin(x)'
       ]


err = 10**-16
#g | 0
name = names[0]
func = FN[0]

#We need x0 to be within M of alpha so we solve for M
#THe calculation for M was done on paper
M = 1.020423789


x0 = 2
TrueResult,n = Better_Error_Newton_Method(func, x0, err, verbose=True);
print(f"f(x) = {name} | n: {n} | X0: {x0} |\
 Root: x = {TrueResult}");
 
x0 = TrueResult-M
result,n = Better_Error_Newton_Method(func, x0, err);
print(f"f(x) = {name} | n: {n} | X0: {x0} |\
 Root: x = {result}");
 
x0 = TrueResult+M
result,n = Better_Error_Newton_Method(func, x0, err);
print(f"f(x) = {name} | n: {n} | X0: {x0} |\
 Root: x = {result}");
 
x0 = 1
result,n = Better_Error_Newton_Method(func, x0, err);
print(f"f(x) = {name} | n: {n} | X0: {x0} |\
 Root: x = {result}");
 
x0 = 3
result,n = Better_Error_Newton_Method(func, x0, err);
print(f"f(x) = {name} | n: {n} | X0: {x0} |\
 Root: x = {result}");
 
"""
From our findings the M says our points the choose x0 need ot be between .875 and 2.915
but we also can see that x0 = 3 works but .875 point did not. This makes sense since
once you pass 1 the x0 is closer to the root that is outside of the interval
Also if you choose one dirrectly it won;t work because the graph is flat 
at that point causing this not to work as well. but we can also see that 3
worked anI would imagine we didn;t include it because it is considered unstable
"""