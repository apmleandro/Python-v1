# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 23:40:17 2020

@author: apmle
"""

''' Esse um codigo para analisar a projecao de PIBs de alguns paises feita pelo FMI em 2014'''

import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('PIB.csv') 

def get_pais():
    getpais=False
    while not getpais:
        pais_any=input("Qual pais voce gostaria de ter informacoes sobre o PIB.\n")
        
        pais=pais_any.lower()
        if pais == 'estados unidos' or pais=='eua':
            pais_any='EUA'
            
        if pais == 'italia':
            pais_any='Itália' 
            
        if pais == 'india':
            pais_any='Índia' 
            
        if pais == 'russia':
            pais_any='Rússia' 
            
        if pais == 'canada':
            pais_any='Canadá' 
            
        if pais == 'mexico':
            pais_any='México'
            
        if pais== 'indonesia':
            pais_any='Indonésia'
            
        if pais == 'china':
            pais_any='China' 
            
        if pais == 'alemanha':
            pais_any='Alemanha' 
            
        if pais == 'reino unido':
            pais_any='Reino Unido' 
            
        if pais == 'franca':
            pais_any='França'
            
        if pais== 'brasil':
            pais_any='Brasil'
        
        if pais == 'coreia do sul':
            pais_any='Coreia do Sul'
            
        if pais== 'espanha':
            pais_any='Espanha'
            
            
        if pais_any not in df.values:        
            cont=int(input("País não disponível. Digite 1 se voce gostaria de tentar outro pais ou 0 caso nao queira.\n"))
            if cont==0:
                break 
        else:
            getpais=True
        
        return pais_any

pais=get_pais()   
    
def get_ano():
    getano=False
    while not getano:
        try:
            ano=int(input("Por favor me diga o ano que voce deseja analisar entre 2013 e 2020.\n"))
            if ano<2013 or ano>2020:
                cant=input("País não disponível. Aperte qualquer tecla se voce gostaria de tentar outro pais ou 0 caso nao queira.\n")
                if cant=='0':
                    break
                else:
                    continue
            else:
                year=str(ano)
                getano=True
        except ValueError:
            print("Me desculpe, eu nao entendi.")
            continue
        return year
    
ano=get_ano()


def run_PIB(ano,pais):
    PIB_ind=df.loc[df['País']==pais, ano].values[0]
    print(f"A previsao do PIB do {pais} em {ano} foi de {PIB_ind}.\n")
     
run_PIB(ano,pais)

def variation(df):
    print("Agora vamos listar, por país, a estimativa de variação do PIB, em percentual, entre os anos de 2013 e 2020.\n")
    for pais_e in df['País'].values:
        curr=df.loc[df['País']==pais_e, '2020'].values[0]
        Ini=df.loc[df['País']==pais_e, '2013'].values[0]
        Var=round((((curr/Ini)-1)*100),2)
        print(f"{pais_e:<20}\tVariacao de {Var}% entre 2013 e 2020.")

variation(df)    


def pib_plot():  
    print("\nAgora vamos plotar a evolucao do PIB.")
    print("Para isso, precisamos saber qual o seu pais de interesse:")
    pais_plt=get_pais()
    anos=[]
    PIB_prog=[]
    for i in range(2013,2021):
        anos.append(i)
        ano_d=str(i)
        prog=df.loc[df['País'] == pais_plt, ano_d ].values[0]
        PIB_prog.append(prog)
    
    plt.plot(anos,PIB_prog,'r-')
    plt.xlabel('Anos')
    plt.ylabel('PIB')
    plt.title(f'Evolucao do PIB no {pais_plt}')
    plt.show()

pib_plot()
   
    
        
        
    

    
    
 




