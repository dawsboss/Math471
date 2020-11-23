#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 08:46:09 2020

Do 3 iterations of Newton's method for f(x) = 3 - e^x, using x0 = 1.
 Repeat, using x0 = 2, 4, 8, 16. Comment on your results
"""
import math
import numpy as np
import matplotlib.pyplot as plt

def derivatice_approx( f, x, h ):
    return ( (f(x+h) - f(x-h))/(h*2) )



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



def Better_Error_Newton_Method( f, x0, err, df=False, verbose = False):
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
                





FN = [
      lambda x: math.exp(-x) - x,
      lambda x: math.cos(x) - x,
      lambda x: 3-math.exp(x),
      lambda x: -math.exp(x)
     ]


names= [
        'e^-x - x',
        'cos(x) - x',
        '3 - e^x'
       ]



err = 10**-4
func = FN[2]
name = names[2]
Dfunc = FN[3]

a = 2

result = Newton_Method(func, a, 3);
print(f"g(x) = {name} | {a} |\
 Root: fx = {result}");
 
 
 
 
err = 10**-4
func = FN[2]
name = names[2]
Dfunc = FN[3]

a = 1

plt.figure(figsize=(20,10))

result = Grapher_Newton_Method(func, a, 10, verbose=True);
print(f"g(x) = {name} | {a} |\
 Root: fx = {result}");
 
Func = np.vectorize(func)

domain1 = .5
domain2 = 1.25

x = np.linspace(domain1, domain2, 100)
y = Func(x)
plt.plot(x,y,
         [domain1, domain2],[0,0])

resultX = []
resultY = []
for i in result:
    y = derivatice_approx(func, i, .000001)*(x-i)+func(i)
    plt.plot(x,y)
    



plt.show()










result,count = Error_Newton_Method(func, 16, 10**-9, verbose=True)
print(f"Result: {result} | count: {count}")


 
 
 