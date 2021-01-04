# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 02:07:37 2020

@author: apmle
"""

'''This is a code to calculated the weighted average of grades of a student '''


grades=[]
weight_list=[]
product=[]

name=input("What is the student name?\n")
i=1
while True: 
    grade=float(input(f"What is the student grade #{i}?\n"))
    grades.append(grade)
    weight=float(input(f"What is the grade weight for the grade #{i}?\n"))
    weight_list.append(weight)
    i+=1
    if i >2:
        break


for g,w in zip(grades,weight_list):
    product.append(g*w)
    media=round((sum(product)/sum(weight_list)),2)

print(f"The weighted average grade of the student {name} was {media}.")
    