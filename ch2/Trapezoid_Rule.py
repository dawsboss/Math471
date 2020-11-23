#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:52:05 2020

@author: grant
2.5
Trapazoid

1.
Use the trapazoid rule with h=1/4 to approx the integral 

I = integral from 0 to 1(x^3 dx) = 1/4

T4 = 17/64, How small does hy have to be for the error to 
be less than 10^-3? 10^-6?

2.
I=integral from 0 to pi/2(sinx dx) = 1

h for 10^-3? 10^-6?
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
    return(b-a)/h


def f1 ( x ):
    return x**3

def f2( x ):
    return math.sin(x)

def hh( a,b,n ):
    return (b-a)/n

a=0
b=1
n=4
h=1/4
result1 = NaiveTrapezoid(a, b, n, f1)
print(f"a={a} | b={b} | n={n} | f(x)=x^3 | n={nn(a,b,h)} | h={hh(a,b,n)} | Result: {result1} | Actual: {1/4}\n")

a=0
b=(math.pi/2)
n=2
h=(math.pi/4)
result2 = NaiveTrapezoid(a, b, n, f2)
print(f"a={a} | b={b} | n={n} | f(x)=sin(x) | n={nn(a,b,h)} | h={hh(a,b,n)} | Result: {result2} | Actual: {1}")



a=0
b=1

print("============================")
print(int(nn(0, 1, .04472))+1)
n=int(nn(0, 1, .04472))+1

result1 = NaiveTrapezoid(a, b, n, f1)
print(f"a={a} | b={b} | n={n} | f(x)=x^3 | h={hh(a,b,n)} | Result: {result1} | Actual: {1/4}\n")

print("============================")
print(int(nn(0, 1, .0014142))+1)
n = int(nn(0, 1, .0014142))+1 

result1 = NaiveTrapezoid(a, b, n, f1)
print(f"a={a} | b={b} | n={n} | f(x)=x^3 | h={hh(a,b,n)} | Result: {result1} | Actual: {1/4}\n")


a=0
b=(math.pi/2)

print("============================")
print(int(nn(0, math.pi/2, .1469952094))+1)
n= int(nn(0, math.pi/2, .1469952094))+1

result2 = NaiveTrapezoid(a, b, n, f2)
print(f"a={a} | b={b} | n={n} | f(x)=sin(x) | h={hh(a,b,n)} | Result: {result2} | Actual: {1}")

print("============================")
print(int(nn(0, math.pi/2, .0046483967))+1)
n=int(nn(0, math.pi/2, .0046483967))+1
result2 = NaiveTrapezoid(a, b, n, f2)
print(f"a={a} | b={b} | n={n} | f(x)=sin(x) | h={hh(a,b,n)} | Result: {result2} | Actual: {1}")