# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:14:29 2019

@author: Adrian
"""

#arr = [3,1,2,2,4]
#
#def customSort(arr):
#    # Write your code here
#    c = []
#    arr.sort()
#    c = sorted(arr,key=arr.count,reverse=False)
#    
#    return c 
#        
#print(customSort(arr))

def missingWords(s, t):
    missing = [];
    a = s.split(' ');
    b = t.split(' ');
    
    missing = list(set(a).symmetric_difference(b))   
   
    
    return missing

s = "I am using HackerRank to improve programming"
t = "am HackerRank to improve"

print(missingWords(s, t))