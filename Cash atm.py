# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:57:31 2020

@author: apmle
"""


''' This is a code for a atm '''
def cash_atm(cash):
    if cash <10:
        print("The minimum amount available to withdraw is $10 dollars")
    elif cash> 600:
        print("The maxinum amount available to withdraw is $600 dollars")
    else:
        unit = cash%10
        five_bill = int(unit/5) #number of 5 dollars bills
        one_bill = int((unit%5)/1) #number of 1 dollar bill
        ten = cash%100 - unit
        fif_bill = int(ten/50) #number of 50 dollars bills
        ten_bill= int((ten%50)/10) #number of 10 dollar bill   
        hund = (cash - unit - ten)
        hund_bill= int(hund/100) #number of 100 dollars bill
    print(f"The amount requested will be dispensed as {one_bill} bills of 1 dollar, {five_bill} bills of 5 dollars, {ten_bill} bills of 10 dollars, {fif_bill} bills of 50 dollars and {hund_bill} bills of 100 dollars.\n" )
        
     
        
while True:
    money= float(input("Hello! Who much cash would you like to withdraw today?\n"))
    cash_atm(money)
    cont=input("Do you wish to withdraw another amount? If yes, type any key, or else type 0.\n")
    if cont =='0':
        break    


# Resolução já utilizando listas e estruturas de repetição
#cedulas = [100, 50, 20, 10, 5, 2, 1]
#min_saque = 10
#max_saque = 600
#valor = 0
#
#while valor < min_saque or valor > max_saque:
#  valor = int(input(f"Informe um valor entre {min_saque} e {max_saque}: "))
#  if valor < min_saque or valor > max_saque:
#    print("Valor inválido.")
#
#i = 0 # índice da lista de cédulas
#while valor > 0:
#  cedula = cedulas[i] # Pelo índice, vejo que tipo de cédula vou usar
#  num_cedulas = int(valor/cedula) # retorna sempre a parte inteira do valor.
#  if num_cedulas > 0:
#    print(f"{num_cedulas} cédula(s) de R${cedula}.")
#    # Calcular quanto falta:
#    valor = valor % cedula # Cálculo via resto da divisão
#  # Também seria possível calcular assim:
#  # valor = valor - num_cedulas * cedula 
#  # print(f"Agora, faltam R${valor}.")
#  i += 1
#
#        
#    
#    
#    
#
