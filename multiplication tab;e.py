# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:20:13 2020

@author: apmle
"""

''' This is a code to display a multiplication table '''

numeros=list(range(1,11))
mult_res=[]
for num in numeros:
    i=1
    storage=[]
    while i<=10:
        mult=i*num
        storage.append(mult)
        i+=1
        if i==10:
            mult_res.append(storage)

print(f"{'Multiplication table':>50}")
for n in mult_res:
    print(*n, sep='\t')




