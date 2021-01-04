# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 00:48:33 2020

@author: apmle
"""


def valid_month(date): 
    if len(date) < 10:
        print("Invalid format. Please enter the date in the following format DD/MM/YYYY")
    elif date[2]!= '/' or date[5]!='/':
        print("Invalid format. Please enter the date in the following format DD/MM/YYYY using '/' to separate the date")
    else:
        dia=int(date[0:2])
        if dia<=0 or dia>31:
            print("Invalid format. Please enter a day between 01 and 31")        
        mes=int(date[3:5])
        if mes<=0 or mes>12:
            print("Invalid format. Please enter a month between 01 and 12")
        else:
            print("The date entered is valid")
            
while True:
    day=input("Please enter the date in the following format DD/MM/YYYY.\n")
    valid_month(day)
    cont=input("Do you wish to enter another date? Type any key for yes, or 0 for no.\n")
    if cont =='0':
        break    
        
        
        

        
        
    





        

