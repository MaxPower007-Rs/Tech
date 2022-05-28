# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 15:56:46 2019

@author: Adrian
"""

#Jumping on the Clouds


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    jump = 0
    n =len(c)
    while i < n-1:
        if i+2 >= n or c[i+2]== 1:
            i= i+1
            jump+=1            
        else:
            i+=2
            jump+=1       
            
    return jump
    
 

c = [0, 0, 0, 0, 1, 0]
c1 = [0, 0, 1, 0, 0, 1, 0]
n = 6
print(jumpingOnClouds(c))