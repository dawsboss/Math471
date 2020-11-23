import math

err = math.pow(10.0, -5.0)
print("err contains: {:8.6f}".format(err))

#Setup approximating value:
A_n = 0.0

#Setup counter variable
i = 0

#Consistant comparing value:
tenth = 1.0/10.0

#Loop over power of 2
while( abs(tenth - A_n) >= err ):
    #Build next p[ower of 2
    a_i = math.pow(2.0, -i)

    if( tenth - A_n - a_i >= 0):
        A_n=A_n+a_i
        print("a_i: {:8.6f}, A_n: {:8.6f}, i: {}".format(a_i, A_n, i))

    #Increment counter variable:
    i = i+1

print("Report on accuracy of the approx {}".format(tenth - A_n))
