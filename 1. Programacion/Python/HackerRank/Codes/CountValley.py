# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 18:31:30 2019

@author: Adrian
"""

def countingValleys(n, s):
    level=valley=0
    for i in range(n):
        if(s[i]== "U"):
            level+=1
            if(level==0):
                valley+=1
        else:
            level-=1
        
    return valley

s = ["D","D","U","U","D","D","U","D","U","U","U","D"]
n = 12

s1 = "UDUUUDUDDD"  #0
n1 = 10

n3 = 8
s3 = "UDDDUDUU"   #1

n4= 10
s4 = "DUDDDUUDUU"   #2

n5 = 10
s5 = "DDUDDUUDUU"  #1

print(countingValleys(n5, s5))