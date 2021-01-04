# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 05:02:16 2020

@author: apmle
"""

#Questao3
#Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 
#participantes e suas respectivas notas, variando de 0 até 10. Crie uma função
# que leia os nomes dos participantes e, ao final, apresente apenas o nome e a 
# nota do vencedor.
#
#Fluxo de exceção: 
#
#O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor 
#ou igual a dez.

print("Today we will decide who was the winner of the costume contest.\n")

cont=False
nomes=[]
pontos=[]
while True:
    try:
        comp=int(input("Please, tell me how many competitors are participating in the costume contest:\n"))
        if comp <0:
            print("Please enter valid amount of participants. The number should be higher than zero.")
            continue
        if comp==0:
            print("Seems like there are no participants in this competitions. Is that right?")
    except ValueError:
        print("Sorry, I didn't understand that. Please enter a number higher than zero")
        continue
    else:
        break

def winner_contest(comp):
    for i in range(1,comp+1):
        nome=input(f"Please enter the name of the competitor #{i}.\n")
        nomes.append(nome)
        while True:
            try:
                total=float(input(f"Please enter the total amount of points {nome} received.\n" ))
                if total <0 or total>10:
                    print("Please enter amount of point. The points range from 0 to 10.")
                    continue
            except ValueError:
                print("Sorry, I didn't understand that. Please enter a number between 0 and 10.")
                continue
            else:
                pontos.append(total)
                break
    winner_point=max(pontos)
    idx=pontos.index(winner_point)
    winner=nomes[idx]
    print(f"The winner was {winner} with {winner_point} points.")

winner_contest(comp)
    
    