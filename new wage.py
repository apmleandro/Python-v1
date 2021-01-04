# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:57:09 2020

@author: apmle
"""

''' This is a program to calculate and display new wage '''

def new_salary(wage):
        if wage <= 1000:
            new_wage = wage + wage*0.30
        elif wage > 1000 and wage <=2000:
            new_wage = wage + wage*0.25
        elif wage > 2000 and wage <=3000:
            new_wage = wage + wage*0.20    
        elif wage > 2000 and wage <=3000:
            new_wage = wage + wage*0.20
        elif wage > 3000 and wage <=4000:
            new_wage = wage + wage*0.15  
        elif wage > 4000:
            new_wage = wage + wage*0.10
        print(f"Your new salary is {new_wage}.")
    
while True:
    salary=float(input("Please enter your current salary.\n"))
    new_salary(salary)
    cont=input("Do you wish to type another salary? If no type 0, if yes type any key")
    if cont =='0':
        break



    
    
    
    
    
    
    
    


