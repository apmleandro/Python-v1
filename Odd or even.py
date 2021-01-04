# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 14:42:43 2020

@author: apmle
"""

'''This program is to know whether the number is odd or even'''


while True:
    number=float(input("Please enter a number:\n"))
    rest=number%2
    if rest != 0:
        print(f"The number {number} is a odd number")
    elif rest == 0:
        print(f"The number {number} is a even number")
    cont=float(input("Do you wish to enter another number? Type 1 for yes or type 0 for no:\n"))
    if cont == 0:
        break
    