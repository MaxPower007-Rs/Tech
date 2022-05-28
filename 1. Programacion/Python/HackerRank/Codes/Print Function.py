# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:36:18 2019

@author: Adrian
"""

'''
Read an integer N.
Without using any string methods, try to print the following:
123...N
Note that "..." represents the values in between.
'''
n = int(input())

# Code
count = 0
strCount = []
for i in range(n):
    count+=1
    strCount.append(str(count))
    
# Print values one by one,  means array is unpacked
print(*strCount, sep='', end='\n')