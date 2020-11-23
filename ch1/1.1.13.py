# Problem 1.1.13

# "Construct a Taylor polynomial approximation that is accurate to within 10^-6, 
#   over the indicated interval, for each of the following functions, using x0 = 0"

#13a. f(x) = sin(x), x = [0,1]
#13b. f(x) = e^-x, x=[0,1]
#13c. f(x) = ln(x+1), x=[0,.75]

import math


#Function to approximate exp(x) (that is, e^x), based on given
#   degree (n) for approximating polynomial, centered at zero'
#   x is expected argument contain the value to be "plugged in"
#   n is the degree of the poly approx
def approxE( x, n ):
    retval=0.0
    
    #Create polly approx of given degree n:
    for k in range(0,n+1):
        retval = retval + math.pow(-1,k) * (math.pow(x,k)/math.factorial(k))
    
    return retval


#Function to approximate sin(x), based on given
#   degree (n) for approximating polynomial, centered at zero'
#   x is expected argument contain the value to be "plugged in"
#   n is the degree of the poly approx
def approxSin( x, n ):
    retval=0.0
    
    #Create polly approx of given degree n:
    for k in range(0,n+1):
        retval = retval + ( (math.pow(-1,k)*math.pow(x,(2*k)+1) )/ math.factorial((2*k)+1))
    
    return retval


#Function to approximate ln(x+1), based on given
#   degree (n) for approximating polynomial, centered at zero'
#   x is expected argument contain the value to be "plugged in"
#   n is the degree of the poly approx
def approxLN( x, n ):
    retval=0.0
    
    #Create polly approx of given degree n:
    for k in range(1,n+1):
        retval = retval + ( (math.pow(-1,k+1)*math.pow(x,k) )/ (k) )
    
    return retval










#create some varriables 
domainval = 1
degree = 9

#Call function and store results
result = approxE( domainval, degree )

#Stores the correct answer
reference = math.exp(-domainval)


#print results
print("Degree {} | approximation of e^-x is: {}".format( degree, result))

#print the correct answer
print("Reference for e^-x: {}".format( math.exp(-domainval) ))

print("Amount of error for e^-x: {0:.15f}\n".format(reference - result))



domainval = 1
degree = 5
result = approxSin( domainval, degree )
reference = math.sin(domainval)

print("Degree {} | Approximation of sin(x) is: {}".format( degree, result ))

print("Reference for sinx: {}".format( reference ))

print("Amount of error for Sinx: {0:.15f}\n".format( reference - result ))



domainval = .75
degree = 36
result = approxLN( domainval, degree )
reference = math.log(domainval+1)

print("Degree {} | Approximation of ln(x+1) is: {}".format( degree, result ))

print("Reference for sinx: {}".format( reference ))

print("Amount of error for ln(x+1): {0:.15f}\n".format(reference - result))