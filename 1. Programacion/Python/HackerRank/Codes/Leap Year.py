# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:12:47 2019

@author: Adrian
"""
"""
We add a Leap Day on February 29, almost every four years. The leap day is an extra, 
or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, 
while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years
"""
def is_leap(year):
    leap = False
    calc = year%4
    calc2 = year%400
    calc3 = year%100

    if calc == 0:
        if calc3 == 0:
            if calc2 == 0:
                leap = True
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))