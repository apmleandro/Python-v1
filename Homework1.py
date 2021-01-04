# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:20:13 2020

@author: apmle
"""

# Homework#1

#Questao 1
#Crie um algoritmo que receba, como entrada, o valor de três notas de um aluno - com valor entre 0 e 10, e, em seguida, informe a média entre elas. 
#Neste momento, não é necessário validar se a nota está dentro do intervalo válido!

#Minha solucao
nota_1=int(input("Informe sua nota ")) # Correcao --> se eu deixar int, o usuario nao poder colocar numero quebrado. O ideal e usar float que me da numeros reais
nota_2=int(input("Informe sua nota "))
nota_3=int(input("Informe sua nota "))


def media_alunos(nota_1,nota_2,nota_3):
    media = (nota_1 + nota_2 + nota_3)/3 # Posso arrendondar a media para quantas casa decimais eu quero ter
    #tambem posso converter parte da variavel 
    return f"A media dos alunos e {media}." # Peguntar se criar funcao demora mais? 


q= media_alunos(nota_1,nota_2,nota_3)
print (q)
    
#Solucao prof
nome = input("Nome do(a) aluno(a): ")
# Vamos criar três variáveis, chamadas av1, av2, av3
# Determinar qual é o valor de av1
av1 = float(input("Informe a nota da AV1: "))
# Determinar qual é o valor de av2
av2 = float(input("Informe a nota da AV2: "))
# Determinar qual é o valor de av3
av3 = float(input("Informe a nota da AV3: "))
# Cálculo da média
media = ( av1 + av2 + av3 ) / 3 # Para 8.5, 9.5 e 8 retorna 8.66666666
# Para o caso de dízimas periódicas, arredondaremos o valor da média
media = round(media, 2) # arredonda a média com duas casas decimais.
# Criaremos nova variável com versão da média em texto, com vírgula como separador decimal.
media_formatada = str(media).replace('.',',') 
# Saída para o usuário usando a média formatada
print(f"O(A) aluno(a) {nome} obteve média {media_formatada}.")

