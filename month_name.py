# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:47:05 2020

@author: apmle
"""

'''This a program to read an integer and correlate to the corresponding month'''


def get_month(mes):
    if mes <1 or mes >12:
        print("Please type a valid month between 1 and 12.\n")
    else:
        number=[1,2,3,4,5,6,7,8,9,10,11,12]
        month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        Month= zip(number,month)
        Monthset = dict(set(Month)) #creates a dictionary of the pairs -- set creates the tuples
        Result_month = Monthset[mes]
        print(f"The corresponding month is {Result_month}.\n")
        
while True:
    mes=int(input("Please type the number corresponding to the month of the year you would like know.\n"))
    get_month(mes)
    cont=input("Do you wish to enter another month? If yes, type any key, or else type 0.\n")
    if cont =='0':
        break
    
    
    
           
#    if mes <1 or mes >12:
#        print("Please type a valid month between 1 and 12.\n")
##    if mes in number:
##        ind= number.index(mes)
##        mes_corresp= month[ind]
##        print(f"The corresponding month is {mes_corresp}.\n") 
#


          
    