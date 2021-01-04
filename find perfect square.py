#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:45:24 2020

@author: analeandro
"""

#Crie um algoritmo que analise uma lista de números aleatórios e informe quantos e 
#quais elementos são um quadrado perfeito.
# Dica: Lembre-se de que elevar um número a ½ retorna sua raiz quadrada
# Pesquise a função .floor() de Python

#.floor()

'''This is a code to find how many perfect squares are in a random list'''
import random
perfect=[]
num=0
size_list=int(input("Please enter how many elements do you want try"))
l = [random.randint(0,10) for i in range(5)]
for n in l:
    square=n**(1/2)
    if square%1 == 0:
        perfect.append(n)
        num+=1

print(f"There are {num} perfect squares. Those are: ", end='')
print(*perfect, sep=' ')
            
