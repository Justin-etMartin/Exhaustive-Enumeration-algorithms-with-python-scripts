# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:30:43 2026

@author: Dometi Justin Etse
"""

#Using exhaustive emuration to find primality
# Test if an int > 2 is prime, if not print the smallest divisor.

x = int(input('Enter an integer greater than 2: '))

smallest_divisor = None

for guess in range(2 , x):
    
    if x%guess ==0:
        
        smallest_divisor = guess;
        
        break
    
if smallest_divisor != None:
    print('the smallest divisor of', x, 'is', smallest_divisor)
else:
    print(x,'is prime')