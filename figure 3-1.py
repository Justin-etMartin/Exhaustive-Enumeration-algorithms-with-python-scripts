# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:52:33 2026

@author: Dometi Justin Etse
"""
#FIND THE CUBE ROOT OF AN INTERGER

x = int(input('Enter an integer: '))
ans = 0

while ans**3 < abs(x):
    # print('Value of the decrementing function abs(x) - ans**3 is', abs(x) - ans**3)
    # ans = ans + 1
    #ans = ans #Now, restore the
# initialization of ans, replace the statement ans = ans + 1 by
# ans = ans, and try finding the cube root of 8. 
    
if ans**3 != abs(x): #alignment error leads to the repetition of this if statement print function till the while condition is met if most cases
    
 print(x,'is not a perfect cube')
       
else:
    if x < 0 :
        ans = -ans
    print ('the cube of',x,'is', ans)
    