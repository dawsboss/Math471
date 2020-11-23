# -*- coding: utf-8 -*-
"""
Grant Dawson
1.5.9
"""
import math
import matplotlib.pyplot as plt
import numpy as np

def dirivOfOneOverX(n, x):#n is the what dirivate you are taking
                            #x is the number it will be f^k of
    return math.pow(-1, n) * math.factorial(n) * math.pow(x, n+1)
    

def approxOneoverX(Xo, X, n):
    sum = 0.0
    for i in range(0,n+1):
        sum += (float)((math.pow(X-Xo, i)) * dirivOfOneOverX(i, Xo))/math.factorial(i)

    return sum




xNot = 1
x = .5
degree = 5

print("Actual answer: ",1/x)
print(approxOneoverX(xNot, x, degree))
print("error ", 1/x - approxOneoverX(xNot, x, degree))



#Created the domain space
t = np.linspace(.5,1, num=100, endpoint=True)

#Create range for our plot
y = np.array([approxOneoverX(xNot, x, 50) for x in t])
realY = np.array([1/x for x in t])
errorY = np.array([(1/x - approxOneoverX(xNot, x, degree)) for x in t])

plt.figure()
plt.plot(t, realY, label='Real')
plt.plot(t,y,label='f(x)')
plt.legend()
plt.show()

plt.figure()
plt.plot(t, errorY, label='Error')
plt.legend()
plt.show()