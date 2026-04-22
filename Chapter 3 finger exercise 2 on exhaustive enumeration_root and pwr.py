# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:00:31 2026

@author: Dometi Justin Etse
"""

# Finger exercise: Write a program that asks the user to enter an
# integer and prints two integers, root and pwr, such that 1 < pwr < 6
# and root**pwr is equal to the integer entered by the user. If no such
# pair of integers exists, it should print a message to that effect.



#User input request      
x = int(input('Enter an integer: '))

#Initializing variables and range
for pwr in range(2, 6):  # 1 < pwr < 6
    root = 0

#Initializing loop and iteration logic
    while root**pwr <= abs(x):
        if root**pwr == abs(x):
            if x < 0 and pwr % 2 == 1:  # handle negative numbers
                root = -root
            print('The two integers are', root, 'and', pwr)
            break
        root += 1

    if root**pwr == abs(x):
        break
else:
    print('No such pair of integers exists.')