# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 03:30:09 2020

@author: apmle
"""

salario = float( input("Informe o salário: ") )

if salario <= 1000:
  salario = salario * 1.3
elif salario <= 2000:
  salario = salario * 1.25
elif salario <= 3000:
  salario = salario * 1.2
elif salario <= 4000:
  salario = salario * 1.15 
elif salario < 0:
  print("Valor de salário inválido.") 
else:
  salario = salario * 1.1

salario_info = f"{salario:.2f}" # salario_info = "{0:.2f}".format(salario)