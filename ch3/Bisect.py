#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: grant

Use Algorithm 3.2 to solve the nonlinear equation x = cos(x). 
Choose your own initial interval by some judification 
experimentation with a calculator 

a) 0 = cos(x) - x

"""

import math
#import scipy.optimize.bisectas as bi
import matplotlib.pyplot as plt
import numpy as np

FN = [
      lambda x: math.exp(-x) - x,
      lambda x: math.cos(x) - x
     ]

R = [
     [-1.0, 1.0],
     [-5.0, 5.0],
     [-.5 , .5],
     [-20.0, 20.0]
    ]

names= [
        'e^-x - x',
        'cos(x) - x'
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
        #if(verbose):
        print(f"n:{n}")
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
    
    
    
err = 10**-4
func = FN[1]
name = names[1]


a = R[2][0]
b = R[2][1]

result = bist(func, a, b, err, verbose=False);
print(f"g(x) = {name} | [{a}, {b} |\
 Root: fx = {result}");
 
 
 
a = R[3][0]
b = R[3][1]    
result = bist(func, a, b, err, verbose=False);

print(f"g(x) = {name} | [{a}, {b}] |\
 Root: fx = {result} | \
g(fx) = {FN[1](result)}");




a = R[1][0]
b = R[1][1]
result = bist(func, a, b, err, verbose=False);
print(f"g(x) = {name} | [{a}, {b}] |\
 Root: fx = {result} | \
g(fx) = {FN[1](result)}");





a = R[0][0]
b = R[0][1]    
result = bist(func, a, b, err, verbose=False);

print(f"g(x) = {name} | [{a}, {b}] |\
 Root: fx = {result} | \
g(fx) = {FN[1](result)}");

x = np.linspace(-np.pi, np.pi, 100)
y = np.cos(x)-x


plt.plot(x,y,'b', 
         result,FN[1](result),'ro',
         [-np.pi, np.pi],[0,0])

plt.show()











def bistGrapher(f, a, b, eps, verbose = True):
    #compute some values that are reused often
    fa = f(a)
    fb = f(b)
    
    #check that we have a chance to succeed
    if(fa*fb < 0):#This means it crossed over the x axis
        n = int((math.log(b-a) - math.log(eps)) / math.log(2))+1
        #if(verbose):
        rtnc = []
        rtna = []
        rtnb = []
        print(f"n:{n}")
        for i in range(1, n+1):
            c = a + .5*(b-a)
            rtnc.append(c)
            rtna.append(a)
            rtnb.append(b)
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
        return (rtnc, rtna, rtnb)
    
    else:
        print("No roots in interval")
        return False


#gA = -.1
#gB = 1
x = np.linspace(a, b, 100)
y = np.cos(x)-x

Cs, As, Bs = bistGrapher(func, a, b, err, verbose=False);
zero = [0 for i in Cs]
one = [.05 for i in Cs]
two = [.1 for i in Cs]

plt.figure(figsize=(20,10))
plt.plot(x,y,'b')
plt.scatter(Cs,zero,marker=11)
plt.scatter(As,zero,marker=9)
plt.scatter(Bs,zero,marker=4)
for i in range(0, len(As)):
    plt.annotate(f"A{i}", xy=tuple(zip(As, zero))[i], xytext=tuple(zip(As, zero))[i])
    plt.annotate(f"B{i}", xy=tuple(zip(Bs, zero))[i], xytext=tuple(zip(Bs, one))[i])
    plt.annotate(f"C{i}", xy=tuple(zip(Cs, zero))[i], xytext=tuple(zip(Cs, two))[i])


plt.show()

print()

"""

x = np.linspace(.69, .8, 100)
y = np.cos(x)-x

Cs, As, Bs = bistGrapher(func, .7, .8, err, verbose=False);

del Cs[:5]
del Bs[:5]
del As[:5]

zero = [0 for i in Cs]
one = [.1 for i in Cs]
two = [.2 for i in Cs]

plt.figure(figsize=(20,10))
plt.plot(x,y,'b')
plt.scatter(Cs,zero,marker=11)
plt.scatter(As,zero,marker=9)
plt.scatter(Bs,zero,marker=4)
for i in range(0, len(As)):
    plt.annotate(f"A{i}", xy=tuple(zip(As, zero))[i], xytext=tuple(zip(As, zero))[i])
    plt.annotate(f"B{i}", xy=tuple(zip(Bs, zero))[i], xytext=tuple(zip(Bs, one))[i])
    plt.annotate(f"C{i}", xy=tuple(zip(Cs, zero))[i], xytext=tuple(zip(Cs, two))[i])


plt.show()
"""

