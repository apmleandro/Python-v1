# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:10:00 2020

@author: apmle
"""

#Lista 1

#3 notas de alunos com valor de 0 a 10 informe media
''' This is a code to calculate the average grade of three students'''
notas=[]
nomes=[]
print("What is the student name?")
nome = input()
i=1
while i < 4:
    print(f"What is the student grade # {i}?")
    nota = float(input ())
    if nota < 0 or nota >10:
        print("This grade is out of range. Please type a grade between 0 and 10")
    else:
        notas.append(nota)
        media=round(sum(notas)/i,2)
        i += 1

print(f"A final grade of the student {nome} was {media}" )

    
    
#soma = 0  
#media = 0     
#for n in range(0,len(notas)):
#    soma += notas[n]
#    n +=1
#    media = soma / n

#media_formatada = str(media).replace('.' , ',')

    

    

        


