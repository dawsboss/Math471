
    # x = f * 2^(Beta):
def binaryTransform(x, n):
    beta = 0
    counter = 0 #make sure we dont go over n degree
    while(x > 1.0 and counter < n):
        x /= 2.0
        beta += 1
        counter+=1
    while(x < .5 and counter < n):
        x*=2
        beta -= 1
        counter+=1

    return(x, beta)

#x=141
#x=25
x=2/5
#x = 1/1000000
f, beta = binaryTransform(x, 3)

# Print result.
print('x = {} is: {} * 2^{}'.format(x, f, beta))
