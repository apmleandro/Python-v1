# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:05:53 2020

@author: apmle
"""
#
#Questão 4
#
#Seja a seguinte citação:

#Osjuros compostos são a força mais poderosa do universo e a maior invenção da humanidade, porque permitem uma confiável e sistemática acumulação de riqueza
#
#A frase, curiosamente, é de Albert Einstein, não de algum banqueiro ou gestor de fundos de capitais. 
#
#Assim, suponha que você possui R$10.000 iniciais, consegue aportar R$1.000 por mês e obtém um rendimento de 0,54% ao mês. Por simplicidade, suponha que você faz o aporte após o rendimento no período acontecer.
#
#No primeiro mês, terá R$10.000 + 0,54% deste valor = R$10.054,00. E, com o novo aporte, R$11.054,00.
#
#No segundo mês, o valor inicial é de R$11.054,00. Ele rende 0,54%, totalizando R$11.113,69. Com o novo aporte, R$12.113,69, e assim sucessivamente.
#
#Ao final de 120 meses, você terá o montante final de R$187.303,05.

#Crie um programa que ponha a hipótese de Einstein à prova. Em uma função, receba, 
#como entrada, um montante financeiro inicial, um percentual de rendimento por período, 
#um valor de aporte para cada período e uma quantidade de períodos.
#


import matplotlib.pyplot as plt
import pandas as np


def get_data():
    while True:
        try:
            Val=int(input("Por favor, me diga quanto reais voce gostaria que fizessemos uma estimativa de rendimento?:\nR$"))
            if Val<0:
                print("Por favor escreva um valor maior que 0")
                continue
        except ValueError:
            print("Desculpa, eu nao entendi. Por favor, escreva um valor em reais acima de R$ 0,00.")
            continue
        else:
            break
    
    while True:
        try:
            Rend=float(input("Por favor nos diga qual o percentual de rendimento por mes:\n"))
            if Rend<0:
                print("Por favor escreva um valor maior que 0")
                continue
        except ValueError:
            print("Desculpa, eu nao entendi. Por favor, escreva um valor em reais acima de 0,00%.")
            continue
        else:
            break
    
    while True:
        try:
            Aporte=int(input("Por favor nos diga qual o aporte para cada mes.\nR$"))
            if Aporte<0:
                print("Por favor escreva um valor maior que 0")
                continue
        except ValueError:
            print("Desculpa, eu nao entendi. Por favor, escreva um valor em reais acima de R$ 0,00.")
            continue
        else:
            break
    
    while True:
        try:
            meses=int(input("Por favor, nos diga o numero total de meses voce gostaria que fizessemos uma estimativa de rendimento?\n"))
            if meses<0:
                print("Por favor escreva um valor maior que 0")
                continue
        except ValueError:
            print("Desculpa, eu nao entendi. Por favor, escreva uma quantidade maior que 0.")
            continue
        else:
            break
    
    return Val,Rend,Aporte,meses


def calc_einstein(Val,Rend,Aporte,meses):
    valor_mes=[]
    i=0
    while i<meses:
            Val=Val+Val*(Rend/100)
            Val=round(Val+Aporte,2)
            valor_mes.append(Val)
            print(f"( Apos {i+1} meses, você terá o montante final de {valor_mes[i]}.")
            i+=1
                        

    return valor_mes

#running program
v,r,a,m=get_data()   
values=calc_einstein(v,r,a,m)

months=[]

for x in range(m):
    months.append(x+1)

#Plotting data


x=plt.plot(months,values,'r')
plt.xlabel('Months')
plt.ylabel('Money earned')
plt.title('Money Progession')
plt.legend("A1")
plt.show()





#Crie uma função que exiba um gráfico da evolução do valor acumulado, tendo como eixo das abscissas (horizontal) o número de períodos e, no eixo das ordenadas (vertical), o valor acumulado, em reais.