# -*- coding: utf-8 -*-
"""
Grant Dawson

Problem 1.3.10

"Using the computer and language of you choice. 
    write a program to estimate the machine epsilon."

"""

import math
import sys



#Loop over successively smaller 2-adic numbers:
for i in range(70):
    # 2-adiv fractions for approximating epsilon
    
    small_num = math.pow(2.0, -i)

    if ( 1.0 == 1.0 + small_num ):
        #small_num is <= machine epsilon
        
        #Report out the value of small_num and 1+small_num
        print("i = {}, small_num = {:18.16f}, 1 + small_num = {}"\
              .format(i,small_num, 1.0+small_num))
    else:
        #small_num > machine_epsilon
        
        #Report out the values as we move towards machine epsilon
        print("i = {}, small_num = {:24.22f}, 1 + small_num = {}"\
              .format(i,small_num, 1.0+small_num))
        
print(sys.getsizeof(small_num))

print(sys.float_info.epsilon) 
        