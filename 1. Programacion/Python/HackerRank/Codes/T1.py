# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:33:02 2019

@author: Adrian
"""

def findNumber(arr, k):
    i = 0
    n = 0
    answer = ""
    n = len(arr)
    while i <(n-1):
        if k == arr[i]:
            answer = "YES"
            i=n-1
        else:
            i=i+1                   
            if i == (n-1):            
                answer = "NO"
                
        
    return answer        

arr = [5,1,2,3,4,5,1]
k = 2

print(findNumber(arr, k))