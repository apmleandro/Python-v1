# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:36:04 2020

@author: apmle
"""

'''This is a code to calculate and display the factorial of a number'''

number=int(input("Please enter the number you wish to calculate the factorial of.\n"))
i=1
f=1
while i<=number:
    f*=i 
    i+=1
print(f"{number}!={f}.")