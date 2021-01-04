# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 03:12:34 2020

@author: apmle
"""
0
''' This is a code to read a number and display whether the numbers are positive or negative '''


number=float(input("Please enter a number:\n"))
if number < 0:
    print(f"The number {number} is a negative value")
elif number ==0:
    print(f"The number {number} entered is zero")    
elif number >0:
    print(f"The number {number} entered is a positive value")


