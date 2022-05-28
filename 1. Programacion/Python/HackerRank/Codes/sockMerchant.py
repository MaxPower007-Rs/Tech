# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:42:50 2019

@author: Adrian
"""

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    i=0
    ar.sort()
    while i<(n-1):
        if ar[i]==ar[i+1]:
            count+=1
            i+=2
        else:
            i+=1
    return count

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9

print(sockMerchant(n,ar))