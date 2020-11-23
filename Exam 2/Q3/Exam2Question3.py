#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: grant dawson

Question #3

"""

import math
#import scipy.optimize.bisectas as bi
import matplotlib.pyplot as plt
import numpy as np

FN = [
      lambda x: math.pow(x, math.pow(x,x)) - 3,
     ]

names= [
        'x^x^x - 3'
       ]



#This verrsion must be given n but we can cmpute n if we have the error tolerance
#   n = (log(b-a)-log(eps)) / log(2)
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
        return (c,n)
    
    else:
        print("No roots in interval")
        return False
    
    
    
err = 10**-5
func = FN[0]
name = names[0]


a = 1
b = 2

result, n = bist(func, a, b, err, verbose=False);
print(f" Bisection f(x) = {name} | [{a}, {b}] |\
 Root: fx = {result} itteration: {n}");
 
 
 
 
 
 
 
print()
print()
def Error_Newton_Method( f, x0, err, df=False, verbose = False):
    rtn = x0
    count = 0
    old = 0.0
    if(df):
        while(count<10000):
            count = count +1
            old = rtn    
            rtn = rtn - (f(rtn) / df(rtn))
            if(abs(rtn-old) < err):
                break
            
    else:
        df = derivatice_approx
        while(count < 10000):
            count = count +1            
            old = rtn
            rtn = rtn - (f(rtn) / df(f, rtn, .000001))
            if(abs(rtn-old) < err):
                break
    
    return (rtn,count) 
 
def derivatice_approx( f, x, h ):
    return (8.0*f(x+h) - 8.0*f(x-h) - f(x+2.0*h) + f(x-2.0*h)) / (12.0*h)



err = 10**-5
func = FN[0]
name = names[0]
x0 = 1

result, n = Error_Newton_Method(func, x0, err);
print(f" Newton's Method f(x) = {name} | x0: {x0} |\
 Root: fx = {result} itteration: {n}");




print()
print()
def regularFalsi(f, a, b, err):
    fa = f(a)
    fb = f(b)
    count = 0
    rtn = 0.0
    
    while(count < 10000):
        count = count +1            
        old = rtn
        rtn = (a*fb - b*fa) / (fb - fa)
        fr = f(rtn)
        
        if(abs(fr) < err):
            break
        
        if(fa*fr > 0):
            a = rtn
        else:
            b = rtn
    return (rtn, count)



err = 10**-5
func = FN[0]
name = names[0]
a = 1
b = 2

result, n = regularFalsi(func, a, b, err);
print(f" regular Falsi f(x) = {name} | [{a}, {b}] |\
 Root: fx = {result} itteration: {n}");


























