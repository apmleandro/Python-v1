# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 17:53:40 2020

@author: apmle
"""

#Questao 3
#Crie um algoritmo que recebe o valor da altura e do peso de uma pessoa e retorna seu IMC. 
#IMC = peso / altura² 

nome= input("Qual o seu nome ")
print(f"Ola {nome}!")
print("Por favor, me digite qual unidade voce gostaria usar")
unit=int(input("Digite 1 para unidades em USC ou 2 para unidades em SI "))

if unit == 1:
    altura_ft= float(input("Feet: "))
    altura_in= float(input("Inches: "))
    altura_usc= altura_ft*12 + altura_in
    peso_lb= float(input("Pounds: "))
    BMI_US= (peso_lb/(altura_usc**2)) * 703
    BMI_US=round(BMI_US,2)
    print(f"{nome}, Your BMI e' {BMI_US}")
    if BMI_US <= 16:
        print("You have severe thiness")
    elif 16< BMI_US <= 17:
        print("You have moderate thiness")
    elif 17 < BMI_US <= 18.5:
        print("You have mild thiness")
    elif 18.5< BMI_US <= 25:
        print("You are in the normal wwight range")  
    elif 25 < BMI_US <= 30:
        print("You are overweight")
    elif 30< BMI_US <= 35:
        print("You have Obese Class I")  
    elif 35< BMI_US <= 40:
        print("You have Obese Class II")
    elif BMI_US > 40:
        print("You have Obese Class III")

elif unit ==2:
    altura_m= float(input("Por favor, me diga qual a sua altura em metros "))
    peso_kg= float(input("Por favor, me diga seu peso em kilos "))
    
    IMC_kg= peso_kg/(altura_m**2)
    IMC_kg=round(IMC_kg,2)
    print(f"{nome} seu IMF e' {IMC_kg}")
    
    if IMC_kg <= 16:
        print("Voce esta severamente magro(a)")
    elif 16< IMC_kg <= 17:
        print("Voce esta moderamente magro(a)")
    elif 17 < IMC_kg <= 18.5:
        print("Voce esta levemente magro(a)")
    elif 18.5< IMC_kg <= 25:
        print("Voce esta com peso normal")  
    elif 25 < IMC_kg <= 30:
        print("Voce esta acima do peso")
    elif 30< IMC_kg <= 35:
        print("Voce tem obesidade classe I")  
    elif 35< IMC_kg <= 40:
        print("Voce tem obesidade classe II")
    elif IMC_kg > 40:
        print("Voce tem obesidade classe III")
else:
    print("Por favor, digite apenas 1 ou 2")
 
    
    
