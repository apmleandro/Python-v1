# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 23:38:04 2020

@author: apmle
"""

#Crie um algoritmo que leia e armazene em listas distintas o nome, a idade e o sexo (letra M ou letra F) de 5 pessoas. 
#Após povoar as listas, o algoritmo deve fornecer um relatório informando: 
#- Quantas mulheres existem no grupo. 
#- Quantos homens existem no grupo. 
#- A média de idade dos homens. 
#- A média de idade das mulheres. 
#- O homem mais velho. 
#- A mulher mais nova. 
#- A pessoa mais velha de todo o grupo, seja homem ou mulher. 
#- A pessoa mais nova de todo o grupo, seja homem ou mulher. 
import numpy as np

nomes=[]
sexos=[]
idades=[]
#
#
def get_data():
    while True:
        nome=input("Please enter your name.\n")
        nomes.append(nome)
        
        idade_test= False
        while not idade_test:
            idade=int(input("Please enter your age:\n"))
            if idade<=0:
                print("Please print a valid age.")
            else:
                idades.append(idade)
                idade_test=True
        
        
        sexo_test=False
        while not sexo_test:
            sexo=input("Please enter your gender. Type M for men, F for women or O for other.\n")
            sexo=sexo.upper()
            if sexo =='M' or sexo== 'F' or sexo== 'O':
                sexos.append(sexo)
                sexo_test=True
            else:
                print("Please enter M, F or O.\n")

        cont=input("Do you wish to enter another name? If yes, type any key, or else type 0.\n")
        if cont =='0':
            break   
    
get_data()

#nomes=['Ana', 'Pedro', 'Bruno', 'Nay', 'Kelly']
#idades=[10,20,30,40,50]
#sexos=['F','M','M','F','O']

print(f"{'===================Final Report==================':>30}")
print(f"{'-------------------------------------------------':>30}")
print(f"{'Name':10}\t|{'Age':>10}\t|{'Gender':>10}")
print(f"{'-------------------------------------------------':>30}")
i=0
while i <len(nomes):
    print(f"{nomes[i]:10}\t|{idades[i]:>10}\t|{sexos[i]:>10}")
    i+=1
    


def count_gender():
    fem=0
    male=0
    other=0
    for e in sexos:
        if e == 'M':
            male+=1
        elif e == 'F':
            fem+=1
        else:
            other+=1
    print(f"There are {male} people who identifies themselves as men.\n")
    print(f"There are {fem} people who identifies themselves as women.\n")
    print(f"There are {other} people who identifies themselves as other.\n")

count_gender()





def avg_age():
    M_age=[]
    F_age=[]
    O_age=[]

    i=0
    while i<len(sexos):
        if sexos[i]== 'M':
            M_age.append(idades[i])       
        if sexos[i]== 'F':
            F_age.append(idades[i]) 
        if sexos[i]== 'O':
            O_age.append(idades[i]) 
        i+=1

    M_avg=np.mean(M_age)
    F_avg=np.mean(F_age)
    O_avg=np.mean(O_age)
    print(f"The average age of men in the list is {M_avg}.\n")
    print(f"The average age of women in the list is {F_avg}.\n")
    print(f"The average age of others in the list is {O_avg}.\n")

 # nao funciona porque ele vai me dar o index to primeiro nome dalista que tem esse sexo   
#    for e in sexos:
#        if e == 'M':
#            idx1=sexos.index(e)
#            M_age.append(idades[idx1])
#        elif e == 'F':
#            idx2=sexos.index(e)
#            F_age.append(idades[idx2])
#        elif e == 'O':
#            idx3=sexos.index(e)
#            O_age.append(idades[idx3])
            
avg_age()

def older_people_gen():
    Old_pep=max(idades)
    idx3=idades.index(Old_pep)
    Oldest=nomes[idx3]
    print(f"The oldest person in the list is {Oldest} and they have {Old_pep} years old.\n")

older_people_gen()    
    
def older_gender():    

    M_age=[]
    F_age=[]
    O_age=[]
    M_person=[]
    F_person=[]
    O_person=[]

    i=0
    while i<len(sexos):
        if sexos[i]== 'M':
            M_age.append(idades[i]) 
            M_person.append(nomes[i])
        if sexos[i]== 'F':
            F_age.append(idades[i])
            F_person.append(nomes[i])
        if sexos[i]== 'O':
            O_age.append(idades[i])
            O_person.append(nomes[i])
        i+=1
            
    Old_men_age=max(M_age)
    idx=M_age.index(Old_men_age)
    Old_men=M_person[idx]
    
    Old_women_age=max(F_age)
    idx=F_age.index(Old_women_age)
    Old_women=F_person[idx]

    Old_other_age=max(O_age)
    idx=O_age.index(Old_other_age)
    Old_other=O_person[idx]

    
    print(f"The oldest men in the list is {Old_men} and he has {Old_men_age} years old.\n")
    print(f"The oldest women in the list is {Old_women} and she has {Old_women_age} years old.\n")
    print(f"The oldest other in the list is {Old_other} and they have {Old_other_age} years old.\n")
    
older_gender()
  
def young_people_gen():
    Yog_pep=max(idades)
    idx=idades.index(Yog_pep)
    Youngest=nomes[idx]
    print(f"The youngest person in the list is {Youngest}.\n")
    
    
def young_gender():
    M_age=[]
    F_age=[]
    O_age=[]
    M_person=[]
    F_person=[]
    O_person=[]

    i=0
    while i<len(sexos):
        if sexos[i]== 'M':
            M_age.append(idades[i]) 
            M_person.append(nomes[i])
        if sexos[i]== 'F':
            F_age.append(idades[i])
            F_person.append(nomes[i])
        if sexos[i]== 'O':
            O_age.append(idades[i])
            O_person.append(nomes[i])
        i+=1
            
    Yog_men_age=min(M_age)
    idx=M_age.index(Yog_men_age)
    Yog_men=M_person[idx]
    
    Yog_women_age=min(F_age)
    idx=F_age.index(Yog_women_age)
    Yog_women=F_person[idx]

    Yog_other_age=min(O_age)
    idx=O_age.index(Yog_other_age)
    Yog_other=O_person[idx]

 
    print(f"The yougest men in the list is {Yog_men} and he has {Yog_men_age} years old.\n")
    print(f"The yougest women in the list is {Yog_women} and she has {Yog_women_age} years old.\n")
    print(f"The yougest other in the list is {Yog_other} and he has {Yog_other_age} years old.\n")
    
young_gender()

