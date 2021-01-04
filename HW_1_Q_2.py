# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 17:27:43 2020

@author: apmle
"""

#Questao 2
#Recrie o algoritmo de cálculo de média das notas, mas, desta vez, calcule a média ponderada, sabendo que a primeira nota possui peso 1, a segunda nota possui peso 2 e a terceira nota possui peso 3.
#Sabendo que a média MP é calculada como
#
#MP = 		N1 * P1 + N2 * P2 + N3 * P3
#	       _____________________________
#	
#			(P1 + P2 + P3)
#
#Onde N são as notas e, P, de seus respectivos pesos.


nome=input("Qual e o seu nome?")
nota_1=float(input("Informe sua nota 1 ")) 
nota_2=float(input("Informe sua nota 2 "))
nota_3=float(input("Informe sua nota 3 "))


def media_alunos(nota_1,nota_2,nota_3):
    media = (nota_1*1 + nota_2*2 + nota_3*3)/(1+2+3) #correcao: preciso especificar? #Para o caso de que tenha outro peso? ou quiser modificar o programa depois?
    media = round(media,2) 
    media = str(media).replace('.',',')
    return f"A media do aluno {nome} e' {media}." # Peguntar se criar funcao demora mais? 

q= media_alunos(nota_1,nota_2,nota_3)
print (q)


#Reposta prof 

# 1º Passo: Quais são as notas?
av1 = float(input("Informe a nota da Avaliação 1: "))
av2 = float(input("Informe a nota da Avaliação 2: "))
av3 = float(input("Informe a nota da Avaliação 3: "))

# 2º Passo: Quais são os pesos das notas?
p1, p2, p3 = 1, 2, 3 

# 3º Passo: Associar notas e pesos para compor o numerador da fórmula
numerador = av1 * p1 + av2 * p2 + av3 * p3 

# 4º Passo: Calcular o denominador da fórmula
denominador = p1 + p2 + p3 

# 5º Passo: Calcular a média
media = numerador / denominador 

# 6º Passo (totalmente opcional): Formatar a saída.
media_arredondada = round(media, 2)
media_formatada = str(media_arredondada)
media_formatada = media_formatada.replace("." , ",")

#Attempt #2
print(f"A média ponderada é: {media_formatada}.")

nome=input("Qual e o seu nome?")
nota_1=float(input("Informe sua nota 1 ")) 
nota_2=float(input("Informe sua nota 2 "))
nota_3=float(input("Informe sua nota 3 "))
p1,p2,p3 =1,2,3

def media_alunos(nota_1,nota_2,nota_3):
    media = (nota_1*p1 + nota_2*p2 + nota_3*p3)/(p1+p2+p3) #preciso especificar? #Para o caso de que tenha outro peso? 
    media = round(media,2) # Arrendondo media para 2 
    media = str(media).replace('.',',')
    return f"A media do aluno {nome} e' {media}." # Peguntar se criar funcao demora mais? 

q= media_alunos(nota_1,nota_2,nota_3)
print (q)

print(f"A média ponderada é: {media_formatada}.")


#Attempt #3
nome=input("Qual e o seu nome?")
nota_1=float(input("Informe sua nota 1 ")) 
nota_2=float(input("Informe sua nota 2 "))
nota_3=float(input("Informe sua nota 3 "))
p1=float(input("Informe o peso da nota 1 ")) # isso faz ser mais time consuming?
p2=float(input("Informe o peso da nota 2 "))
p3=float(input("Informe o peso da nota 3 "))

def media_alunos(nota_1,nota_2,nota_3):
    media = (nota_1*p1 + nota_2*p2 + nota_3*p3)/(p1+p2+p3) #preciso especificar? #Para o caso de que tenha outro peso? #preciso criar numerador e denominador
    media = round(media,2) # Arrendondo media para 2 
    media = str(media).replace('.',',')
    return f"A media do aluno {nome} e' {media}." # Peguntar se criar funcao demora mais? 

q= media_alunos(nota_1,nota_2,nota_3)
print (q)