# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 20:35:03 2020

@author: apmle
"""

'''This is a code to calculate the weighted average your grades'''

grades = []
weight_list =[]
name=input("What is the student name?\n")
i=1
while True:
    print(f"What is the student grade #{i}?")
    grade=float(input())
    if grade < 0 or grade>10:
        print("This grade is out of range. Please type a number between 0 and 10.")
    else:
        print(f"What is the weight of the exam grade #{i}?")
        weight=float(input())
        weight_list.append(weight)
        grades.append(grade)
        print("Would you like to add another grade? If yes, press 1, or else press 0.")
        cont=input()
        if cont == '0':
            break
        else:
            i +=1    
        
def weightavg():
    products=[]
    for g,w in zip(grades,weight_list):
        products.append(g*w)
    avg=round((sum(products)/sum(weight_list)),2)
    print(f"The average grade of the student {name} is {avg}")    
    
weightavg()    
    
    
#    for n in range(len(grades)):
#        element = grade*weight 
#        denominador += weight
#        soma+= element
#        weiavg= soma/denominador
#    print("The weighted average grade of the student{name} is {weiavg}")
#
#weightavg(name)