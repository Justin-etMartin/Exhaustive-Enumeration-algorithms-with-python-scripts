# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:43:22 2026

@author: Dometi Justin Etse
"""
# Finger exercise: Write a program that prints the sum of the prime
# numbers greater than 2 and less than 1000. Hint: you probably want
# to have a loop that is a primality test nested inside a loop that
# iterates over the odd integers between 3 and 999.
total = 0
for x in range (2,999):
    divisor = 2
    
    while divisor < x:
       if x%divisor == 0:
         break
       divisor +=1 
    
    if divisor == x:
       total +=x
print('The total sums of primes are',total)