# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:07:12 2026

@author: Dometi Justin Etse
"""

# Finger exercise: hange the code in 
# Figure 3-2 so that it returns
# the largest rather than the smallest divisor. Hint: if y*z = x and y is
# the smallest divisor of x, z is the largest divisor of x.

# intializing variables
x = int(input('Ente an integer greater than 2: '))
y = None

# intializing the loop
for guess in range(2, x):
    if x%guess ==0:
        y = guess;
        z= int(x/y);
        break
if y != None:
    print('the largest divisor of x', x, 'is', z)
else:
    print(x,'is prime')