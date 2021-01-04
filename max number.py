# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 14:54:22 2020

@author: apmle
"""

'''This is a program to read number and display the highest number'''

numbers=[]
while True:
    number=float(input("Please type a number:\n"))
    numbers.append(number) 
    cont = input("Do you wish to enter another number? Type any key for yes or type 0 for no.\n")
    if cont == '0':
        maior=max(numbers)
        print(f"The highest number entered was {maior}.")
        break
    
        
        
            
        