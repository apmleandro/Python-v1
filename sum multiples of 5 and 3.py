# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:46:58 2020

@author: apmle
"""

#[ProjectEuler.net | Problema #1] Múltiplos de 3 e 5
#Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5, 
#obtemos 3, 5, 6 e 9. A soma desses múltiplos é 23. Encontre a soma de todos os múltiplos de 3 ou 5 abaixo de 1000.

print("This is a code to sum all the multiples of 3 and 5 up to 1000.")
mult=[]
for i in range(1,1000):
    if i%3 ==0 or i%5 ==0:
        mult.append(i)
    else:
        i+=1
        
soma=sum(mult)
print(f"The sum of all multiples of 3 and 5 is {soma}.")