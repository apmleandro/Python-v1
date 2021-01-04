# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 03:25:47 2020

@author: apmle
"""

#Questão 01

#Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar), 
#em reais, considerando o número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.
#Ao usuário do programa serão solicitados o valor total do consumo, em reais, o número total de pessoas
# e o percentual do serviço prestado, entre 0 e 100.

''' This is a program to calculate the tip to be paid at the restaurant'''
import time
from time import gmtime
Time=time.strftime("%Y-%m-%d %H:%M:%S", gmtime())
Time2=int(time.strftime('%H'))

if Time2 < 12 :
     print("Good morning. Today I'm going to help you calculate your restaurant bill.")
if Time2 >= 12 and Time <18:
     print("Good afternoon. Today I'm going to help you calculate your restaurant bill.")
if Time2 >= 18 :
     print("Good evening. Today I'm going to help you calculate your restaurant bill.")
     

rest=input("Please type the restaurant name. \n")

while True:
    try:   
        people=int(input("Please type how many people were eating today.\n"))
        if people <0:
            print("Seems like no one was eating today...Is that right?")
            continue
    except ValueError:
        print("Sorry, I didn't understand that. Please enter a number higher than 0")
        continue
    else:
        break
    
        
while True:
    try:   
        bill=float(input("Please type your bill today: R$ "))
        if bill <0:
            print("Please type a valid bill amount. The value should be higher than 0.")
            continue
    except ValueError:
        print("Sorry, I didn't understand that. Please enter a number higher than 0")
        continue
    else:
        break

while True:
    try:   
        tip=float(input("Please enter how much tip percent your party wish to pay today: "))
        if tip <0:
            print("Please type a valid tip percent. The value should be between 0 and 100")
            continue
    except ValueError:
        print("Sorry, I didn't understand that. Please enter a number higher than 0")
        continue
    else:
        break

    

def Bill(people,rest,bill,tip,Time):
    Tip=(bill*(tip/100))
    Total_Bill=(bill+Tip)
    sep_bill=(Total_Bill/people)
    sep_bill=format((sep_bill), '.2f')
    sep_bill= sep_bill.replace('.',',')
    Total_Bill=format((Total_Bill), '.2f')
    Total_Bill= Total_Bill.replace('.',',')
    tip=format(tip,'.2f')
    tip=tip.replace('.',',')
    bill=format(bill,'.2f')
    bill=bill.replace('.',',')
    
    print(f"Your bill today at the restaurant {rest} was R${bill}.\n")
    print(f"Your party have selected to pay {tip}% tip on your bill.\n")
    print(f"The total amount to be paid by the party after tip is R${Total_Bill}.\n")
    print(f"The total amount to be paid by each member of the party is R${sep_bill}.\n")
    print("Thank you for working with us today.\n")
    print(f"{Time}")
    

Bill(people,rest,bill,tip,Time)