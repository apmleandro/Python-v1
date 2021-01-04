# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:15:27 2020

@author: apmle
"""

'''This is a program to determine a person's financial wellness'''

print("This is a program to determine a person's financial wellnes")




names=[]
wages=[]
houses=[]
transps=[]
education=[]

def get_info():
    name_real=False
    while not name_real:
        name=input("Please enter your name.\n")
        names.append(name)
        name_real=True 
    
    while True:
        try:
            wage=int(input(f"Hello {name}! Please tell me your current wage after taxes:\n$"))
            if wage<0:
                print("Please enter a valid age higher than 0")
                continue
        except ValueError:
            print("I am sorry! I didn't understand this. Please enter a value higher than 0.")
            continue
        else:
            wages.append(wage)
            break
    
    while True:
        try:
            house=int(input(f"Please tell me how much do you spend monthly with housing and utilities. If you don't have any housing related expenses, please type 0.\nR$"))
            if house<0:
                print("Please enter a valid amount. The amount should be higher or equal to 0")
                continue
        except ValueError:
            print("I am sorry! I didn't understand this. Please enter a value higher or equal to 0.")
            continue
        else:
            houses.append(house)
            break
    
    
    while True:
        try:
            edu=int(input(f"Please tell me your education related expenses.If you are not studying please type 0.\n$"))
            if edu<0:
                print("Please enter a valid amount. The amount should be higher or equal to 0")
                continue
        except ValueError:
            print("I am sorry! I didn't understand this. Please enter a value higher or equal to 0.")
            continue
        else:
            education.append(edu)
            break
        
    while True:
        try:
            transp=int(input(f"Please tell me your transportation related expenses.\n$"))
            if transp<0:
                print("Please enter a valid amount. The amount should be higher or equal to 0")
                continue
        except ValueError:
            print("I am sorry! I didn't understand this. Please enter a value higher or equal to 0.")
            continue
        else:
            transps.append(transp)
            break
        
        
        
        
        
        
        
def get_info_port():
    name_real=False
    while not name_real:
        name=input("Por favor me diga seu nome.\n")
        names.append(name)
        name_real=True 
    
    while True:
        try:
            wage=int(input(f"Ola {name}! Por favor me diga qual e o seu atual salario:\nR$"))
            if wage<0:
                print("Porfavor escreva um valor maior ou igual a 0")
                continue
        except ValueError:
            print(" Me desculpe, eu nao entendi! Por favor digite um valor maior ou igual a zero.")
            continue
        else:
            wages.append(wage)
            break
    
    while True:
        try:
            house=int(input(f"Por favor me diga quanto voce gasta por mes com contas de casa. Se voce nao tiver nenhuma, por favor,digite 0.\nR$"))
            if house<0:
                print("Valor invalido.Por favor digite um valor maior ou igual a zero.")
                continue
        except ValueError:
            print("Me desculpe, eu nao entendi! Por favor digite um valor maior ou igual a zero.")
            continue
        else:
            houses.append(house)
            break
    
    
    while True:
        try:
            edu=int(input(f"Por favor, me diga quanto são as despesas relacionadas à educação. Se você não está estudando, digite 0.\nR$"))
            if edu<0:
                print("Valor invalido.Por favor digite um valor maior ou igual a zero.")
                continue
        except ValueError:
            print("Me desculpe, eu nao entendi! Por favor digite um valor maior ou igual a zero.")
            continue
        else:
            education.append(edu)
            break
        
    while True:
        try:
            transp=int(input(f"Por favor, me diga suas despesas relacionadas ao transporte.\nR$"))
            if transp<0:
                print("Valor invalido.Por favor digite um valor maior ou igual a zero.")
                continue
        except ValueError:
            print("Me desculpe, eu nao entendi! Por favor digite um valor maior ou igual a zero.")
            continue
        else:
            transps.append(transp)
            break


def financial_wellness(names,wages,houses,education,transps):
    name=names[0]
    wage=wages[0]
    house=houses[0]
    edu=education[0]
    transp=transps[0]
    
    house_perc,edu_perc,transp_perc=0,0,0
    house_perc=round((house/wage)*100,1)
    edu_perc=round((edu/wage)*100,1)
    transp_perc=round((transp/wage)*100,1)
    house_max=0.30*wage
    edu_max=0.20*wage
    transp_max=0.10*wage
    
    print(f"We have finished your report, {name}!")
    
    print(f"{'============================= Financial Wellness Report ==============================':>30}")
    print(f"{'Expenses':>30}")
    print(f"{'======================================================================================':>30}")
    print(f"{'':>10}\t|{'Wage':>10}\t|{'Housing (R$)':>10}\t|{'Education (R$)':>10}\t|{'Transportation (R$)':>10}\t")
    print(f"{'--------------------------------------------------------------------------------------':>30}")
    print(f"{'Recommended':>10}\t|{wage:>10}\t|{house_max:>10}\t|{edu_max:>10}\t|{transp_max:>10}\n")
    print(f"{'Actual':>10}\t|{wage:>10}\t|{house:>10}\t|{edu:>10}\t|{transp:>10}\n")
    print(f"{'Expenses percentage':>30}")
    print(f"{'======================================================================':>30}")
    print(f"{'':>10}\t|{'Housing %':>10}\t|{'Education %':>10}\t|{'Transportation %':>10}\t")
    print(f"{'----------------------------------------------------------------------':>30}")
    print(f"{'Recommended':>10}\t|{'30.0':>10}\t|{'20.0':>10}\t|{'15.0':>10}\t")
    print(f"{'Actual':>10}\t|{house_perc:>10}\t|{edu_perc:>10}\t|{transp_perc:>10}\n")
    
    print(f"Based on these results we conclude that: \n")
    
    if house_perc > 30:
        print("Your expenses with housing are higher than the recommendation.\n") 
        print("Ideally, the maximum percentage of your wage allocated for housing expenses should be 30 %.\n")
        print(f"That means that the total amount you should spend with housing is R${house_max}.")
    else:
        print(" You expenses with housing are within the recommended range. Good job!")
        
    if edu_perc > 20:
        print("Your expenses with education are higher than the recommendation.\n") 
        print("Ideally, the maximum percentage of your wage allocated for Education expenses should be 20 %.\n")
        print(f"That means that the total amount you should spend with Education is R${edu_max}.")
    else:
        
        print(" You expenses with education are within the recommended range. Keep it up!")
    
    if transp_perc >10:
        print("Your expenses with education are higher than the recommendation.\n") 
        print("Ideally, the maximum percentage of your wage allocated for Education expenses should be 10 %.\n")
        print(f"That means that the total amount you should spend with Education is R${transp_max}.")
    else:
        print(" You expenses with transportation are within the recommended range. Nice!")
        









def financial_wellness_port(names,wages,houses,education,transps):
    name=names[0]
    wage=wages[0]
    house=houses[0]
    edu=education[0]
    transp=transps[0]
    
    house_perc,edu_perc,transp_perc=0,0,0
    house_perc=round((house/wage)*100,1)
    edu_perc=round((edu/wage)*100,1)
    transp_perc=round((transp/wage)*100,1)
    house_max=0.30*wage
    edu_max=0.20*wage
    transp_max=0.10*wage
    
    print(f"Terminamos o seu relatorio, {name}!")
    
    print(f"{'============================= Relatorio de Saude financeira ==============================':>30}")
    print(f"{'Gastos':>30}")
    print(f"{'======================================================================================':>30}")
    print(f"{'':>10}\t|{'Salario':>10}\t|{'Moradia(R$)':>10}\t|{'Educacao (R$)':>10}\t|{'Transporte (R$)':>10}\t")
    print(f"{'--------------------------------------------------------------------------------------':>30}")
    print(f"{'Recomendado':>10}\t|{wage:>10}\t|{house_max:>10}\t|{edu_max:>10}\t|{transp_max:>10}\n")
    print(f"{'Atual':>10}\t|{wage:>10}\t|{house:>10}\t|{edu:>10}\t|{transp:>10}\n")
    print(f"{'Porcentagem de gastos':>30}")
    print(f"{'======================================================================':>30}")
    print(f"{'':>10}\t|{'Moradia %':>10}\t|{'Educacao %':>10}\t|{'Transporte %':>10}\t")
    print(f"{'----------------------------------------------------------------------':>30}")
    print(f"{'Recomendado':>10}\t|{'30.0':>10}\t|{'20.0':>10}\t|{'15.0':>10}\t")
    print(f"{'Atual':>10}\t|{house_perc:>10}\t|{edu_perc:>10}\t|{transp_perc:>10}\n")
    
    print(f"Baseado nesses resultados podemos concluir que: \n")
    
    if house_perc > 30:
        print("Suas despesas com moradia são maiores do que o recomendado.\n") 
        print("O ideal é que a porcentagem máxima de seu salário alocada para despesas de moradia seja de 30 %.\n")
        print(f"Isso significa que o valor total que você deve gastar com moradia é de R${house_max}.")
    else:
        print("Suas despesas com noradia estão dentro da faixa recomendada. Bom trabalho!")
        
    if edu_perc > 20:
        print("Suas despesas com educacao são maiores do que o recomendado.\n") 
        print("O ideal é que a porcentagem máxima de seu salário alocada para despesas com educacao seja de 20 %.\n")
        print(f"Isso significa que o valor total que você deve gastar com educacao é de R${edu_max}.")
    else:
        
        print("Suas despesas com educação estão dentro da faixa recomendada. Continue assim!")
    
    if transp_perc >10:
        print("Suas despesas com transporte são maiores do que o recomendado.\n") 
        print("O ideal é que a porcentagem máxima de seu salário alocada para despesas com transporte seja de 10 %.\n")
        print(f"Isso significa que o valor total que você deve gastar com transporte é de R${transp_max}.")
    else:
        print(" Suas despesas com educação estão dentro da faixa recomendada. Parabens!")        
        
        
        
        
        

def display_menu():
    while True:
        try:
            language= int(input("What is your preferred language?\nEm qual lingua voce gostaria de responder?\n(1) Portuguese\n(2) English\n"))
            if language!=2 and language!=1:
                print("Valor invalido.Por favor digite 1 ou 2")
                print("Invalid number. Please type 1 or 2")
                continue
        except ValueError:
            print("Me desculpe, eu nao entendi! Por favor digite 1 ou 2.")
            print("Sorry, I didn't understand! Please type 1 ou 2.")
            continue
        else:
            break
    return language

option=display_menu()

def run_program(option):
    if option == 1:
        get_info_port()
        financial_wellness_port(names,wages,houses,education,transps)
    else:
        get_info()
        financial_wellness(names,wages,houses,education,transps)

run_program(option)
