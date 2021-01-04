# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 01:36:40 2020

@author: apmle
"""

'''This is a program to convert Temperature in degrees Celsius to degrees Fahrenheit'''

def convert(Celsius):
    F= (Celsius*9/5)+32
    print(f"{Celsius} degrees in Celsius is equivalent to {F} degrees Fahrenheit")
    
while True:
    C=float(input("What is the temperature in degrees Celsius?.\n"))
    convert(C)
    cont=input("Do you wish to make another conversion? Type 1 for yes or 0 for no.\n")
    if cont == '0':
        break
