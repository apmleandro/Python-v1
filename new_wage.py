# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 02:42:52 2020

@author: apmle
"""

'''This is a code calculate wage readjustment '''

name=input("Please type your name.\n")
cur_wage= float(input("Please type current wage.\n"))
inc_perc=float(input("Please enter readjustment in percentage\n"))

def wage_readjust(name,cur_wage,inc_perc):
    new_wage= cur_wage + cur_wage*(inc_perc/100)
    print(f"Hello {name}! Your new adjusted salary is ${new_wage}!")
    
wage_readjust(name,cur_wage,inc_perc)