#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:27:46 2020

@author: grant
"""
import numpy as np 

def squareRoot(a, err, x0=False, verbose=False):
    #Note b must .25<b<=1 and k must be even
    #a = b * 2^k
    b = a
    k = 0
    
    while(not .25<b<=1 or k%2==1):
        if(b>1):#b is bigger than the range
            b/=2
            k+=1
        elif b<.25:#b is smaller than the rnage
            b*=2
            k-=1          
        else:#This means that b is in the range but k is odd
            if .25<(b/2)<=1:
                b/=2
                k+=1             
            elif .25<(b*2)<=1:
                b*=2
                k-=1                        
            else:
                print("something broke")
                break
    if(verbose):
        print(f"a = b * 2^k \n{a} = {b} * 2^{k}")
    return (private_squareRoot(b, err, x0, verbose) * (2**(k/2)))
                
                
        
        
    

def private_squareRoot(b, err, x0=False, verbose=False):
    if not x0:
        x0 = ((2*b)+1)/3
    
    if verbose:
        print(f"x0: {x0}")
    prev = .5*(x0 + (b/x0))
    rtn = .5*(prev + (b/prev)) 
    
    if verbose:
        print(f'Iteration {1}: {prev}')
        print(f'Iteration {2}: {rtn}')
    
    i = 3
    limit = 500
        
    # Divergence and max for itter 
    while  abs(rtn - prev) > err and i < limit:
        prev = rtn
        rtn = .5*(prev + (b/prev)) 
        if verbose:
            print(f'Iteration {i}: {rtn}')
        i += 1

    return rtn  # Return the result.
    
    
a=.24
print(f"sqrt({a}) = {squareRoot(a, 10**-6, verbose=True)}")