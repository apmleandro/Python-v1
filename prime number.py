# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:26:44 2020

@author: apmle
"""
'''This is a code to find prime number in a list'''

lower=int(input("Please enter the lower bound of the range.\n"))
higher=int(input("Please enter the higher bound of the range.\n"))
higher+=1
#numbers=[range(lower,higher,1)] #python does not unpack the range() function
numbers=[*range(lower,higher,1)]
item_to_remove=[0,1,2]
notprime=[]

for item in item_to_remove: #funciona porque nao estou iterando dentro da lista que estou removendo itens
    if item in numbers:
        numbers.remove(item)
        
        
for n in numbers:   
    i=2
    while i<n:
        rest= n%i
        if rest == 0:
            notprime.append(n)
            break
        else:
            i+=1    

for np in notprime:
    if np in numbers:
        numbers.remove(np)

print(f"This list contains {len(numbers)} prime numbers in the range you have chosen. The numbers are: ", end='') 
print(*numbers, sep=', ')
    

            

