# Grant Dawson
# Problem 1.3.1 a-d
#
# "In each problem below, A is the exact value, and Ah is an approximation to A.
#    Find the absolute error and the relative error"
#
#1a. A = pi   |  Ah = 22/7
#1b. A = e    |  Ah = 2.71828
#1c. A = 1/6  |  Ah = .1667
#1d. A = 1/6  |  Ah = .1666



import math




#This will calculate the absolute error
def Absolute_Error(real, experiement):
    return abs(real - experiement)

#This will calculate the relative error     
def Relative_Error(real, experiement):
    return abs( (real - experiement) / real )


A = math.pi
Ah = 22.0/7.0
print("A = {:2.6f}   |  Ah = 22/7".format(math.pi))
print("Absolute error = {:2.6f}  |  Relative Error = {:2.6f}".format(Absolute_Error(A,Ah), Relative_Error(A,Ah)))


A = math.e
Ah = 2.71828
print("A = {:2.6f}    |  Ah = 2.71828".format(math.e))
print("Absolute error = {:2.9f}  |  Relative Error = {:2.9f}".format(Absolute_Error(A,Ah), Relative_Error(A,Ah)))


A = 1.0/6.0
Ah = .1667
print("A = 1/6  |  Ah = .1667")
print("Absolute error = {:2.6f}  |  Relative Error = {:2.6f}".format(Absolute_Error(A,Ah), Relative_Error(A,Ah)))


A = 1.0/6.0
Ah = .1666
print("A = 1/6  |  Ah = .1666")
print("Absolute error = {:2.6f}  |  Relative Error = {:2.6f}".format(Absolute_Error(A,Ah), Relative_Error(A,Ah)))








# Problem 1.3.6
#

sum = 0.0
for i in range(0,200000):
    sum = sum + math.pow(math.e, -14 * (1 - math.pow( math.e, -.05*i )))
print(sum)


sum = 0.0
for i in range(200000,0,-1):
    sum = sum + math.pow(math.e, -14 * (1 - math.pow( math.e, -.05*i )))
print(sum)










