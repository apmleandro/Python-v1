# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:55:50 2020

@author: apmle
"""

'''Progresso aritmetica'''

a1=int(input("Please the first number of the sequence.\n"))
a2=int(input("Please the second number of the sequence.\n"))
d=a2-a1
limit=int(input("Please tell me how long you want your sequence to be.\n"))
i=1
numbers=[a1,a2]
while i<(limit-1):
    term=numbers[i]+d
    numbers.append(term)
    i+=1

print("A progressao aritmetica dessa sequencia e: ",end=' ')
print(*numbers)
