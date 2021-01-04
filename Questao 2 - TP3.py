# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 04:57:06 2020

@author: apmle
"""

#Questão 02

# Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:
#
#Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
#Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).
#Não tem direito a voto (menor de 16 anos).
#Fluxo de exceção: 
#
#O programa deve verificar se a idade da pessoa é maior do que zero.

print("This is a code to inform you whether you are able to vote in Brazil")
name=(input("Please enter you name.\n"))
while True:
    try:
        idade=int(input(f"Hello {name}! Please tell me how old you are:\n"))
        if idade<0:
            print("Please enter a valid age higher than 0")
            continue
    except ValueError:
        print("I am sorry! I didn't understand this. Please enter a value higher than 0.")
        continue
    else:
        break
    
def vote(name,idade):   
    if idade<16:
        yearstovote=16-idade
        print(f"I am sorry {name}! You are too young to vote. You will be able to vote in {yearstovote} years from now. Get ready!")
    if idade>=18 and idade<=70:
        print(f"It is mandatory for you to vote, {name}. Please exercise your right to vote.")
    if idade>=16 and idade<18 or idade>70:
        print(f"Your vote is optional, {name}. However it is always a good idea to vote!")

vote(name,idade)

    
