# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:06:53 2019

@author: Adrian
"""
# input n, equals to size of arr
# input arr eg 2 3 6 6 5 enter---> result 5
# Runner-Up --> subCampeon

n = int(input())
#create a map with n elements, then use list function to pass to array format
arr = list(map(int, input().split())) 

#sort funtion from max to min
arr.sort(reverse=True)

#Selecting runner_up
for i in range(n-1):
    if arr[i]>arr[i+1]:
        print(arr[i+1])
        break

