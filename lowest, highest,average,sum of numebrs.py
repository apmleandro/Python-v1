# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:06:23 2020

@author: apmle
"""

''' This is a code to read a sequence of 5 integers and display the sum, the 
average, the highest and lowest numbr of sequence'''

i=1
numbers=[]
while True:
    number=int(input(f"Please enter the number #{i}.\n"))
    numbers.append(number)
    i+=1
    cont=input("Do you wish to enter another number? Type any key for yes, or 0 for no.\n")
    if cont =='0':
        soma= sum(numbers)
        average = soma/ len(numbers)
        maior= max(numbers)
        menor= min(numbers)
        print(f"The sum of the numbers entered is {soma}.\n")
        print(f"The average of the numbers entered is {average}.\n")
        print(f"The highest number of the numbers entered is {maior}.\n")
        print(f"The lowest number of the numbers entered is {menor}.\n")
        break
