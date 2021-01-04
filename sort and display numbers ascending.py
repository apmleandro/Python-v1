# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 15:36:43 2020

@author: apmle
"""

'''This a code to read number, sort them and display them in ascending order'''

numbers=[]
i=1
while True:
    number= float(input(f"Please type the value #{i}.\n"))
    numbers.append(number)
    cont = input("Do you wish to add another value? If yes type any key, if no type 0. \n")
    i+=1
    if cont == '0':
        numbers.sort()
        print("The numbers in ascending order are", end = ' ')
        print(*numbers, sep=", ") # '*' descompacta lista e retorna todos os elementos da lista e sep e usado para me dizer como eu vou separar os numeros
        numbers.sort(reverse=True)
        print("The numbers in descending order are", end = ' ')
        print(*numbers, sep=", ")
        break

