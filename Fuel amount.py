# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 01:12:04 2020

@author: apmle
"""

'''This is a program to inform how many gallons were used to fuel the car tank based on how many dollars we adde'''

def fuel_gallon(price_gallon,money):
    gallon=round((money/price_gallon),2)
    print(f"You purchased {gallon} gallons of gas at ${price_gallon} using {money} dollars.")
    
while True:
    price=float(input("How much is gallon of regular gasoline at this station?\n"))
    cash =float(input("How much do you intend to spend today?\n"))
    fuel_gallon(price,cash)
    cont=input("Do you wish make another calculation? Type 1 for yes or 0 for no \n")
    if cont == '0':
        break


    
    

