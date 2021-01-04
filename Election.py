#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:48:40 2020

@author: analeandro
"""

# Uma eleição de um órgão profissional foi realizada e concorreram 5 chapas
#  identificadas pelos números de 1 a 5. Crie um algoritmo que lê o número de
#  votos de cada chapa, permitindo apenas números naturais e, ao final, imprima 
#  os resultados, indicando quantos votos cada chapa recebeu e o percentual do 
#  total de votos equivalente, indicando se deve haver segundo turno da eleição, 
#  e quais serão as duas chapas a concorrer no segundo turno caso alguma das 
#  chapas não consiga mais de 50% dos votos totais no primeiro pleito.

chapas=[1,2,3,4,5]
perce_voto=[]
win=0
votos=[]
maior=0
i=1
while i <=len(chapas):
    voto=int(input(f"How many votes there was for party {i}.\n"))
    votos.append(voto)
    i+=1

total_vote=sum(votos)


for v in votos:
    per_v=round((v/total_vote)*100)
    perce_voto.append(per_v)
    

print("Election Results")
print("=====================================================")
print("{Party:>30}\t|Counted Votes\t| Vote percentage")

cont=0

while cont< len(chapas):
    print(f"{(chapas[cont]):>}  |   {votos[cont]} |   {perce_voto[cont]}")
    cont+=1


least=min(perce_voto)
most=max(perce_voto)
idx1=perce_voto.index(most)
first=chapas[idx1] 
winner=0
for p in perce_voto:
    if p > 50:
        idx2=perce_voto.index(p)
        winner=chapas[idx2]
        break
    elif p >least and p <most:
        least=p
        idx3=perce_voto.index(least)
        second=chapas[idx3]

if winner != 0:
    print(f"There won't be a second term. The winner is party {winner}")
else:
    print(f"There will be a second term. The partys that will be running are {first} and {second}.")

#f'{variavel:>30}'




        

