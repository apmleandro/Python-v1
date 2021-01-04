# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 02:20:14 2020

@author: apmle
"""

'''This is a code to calculate binary conversion'''

number=int(input("Please enter number you wish to convert.\n"))
bina=[]
while number/2 > 0:
    div=int(number/2)
    rest=number%2
    bina.append(rest)
    number=div
    
bina.reverse()

#stra=""
#for e in bina:
#    a=str(e)
#    stra= stra + a #To append a string a need to use + not append, because string is not mutable
#print(f"The resulting binary number is {stra}.")
#    
#adicionar um pr um 
str1 = ''.join(str(e) for e in bina) #format is separater.join(element or string). Nesse caso nao temos string entao vamos converter cada elemento da lista em string and depois adicionar a string principal usando o "separator"para separar os elementos da string. Eu posso escolher qualquer separator
print(f"The resulting binary number is {str1}.")