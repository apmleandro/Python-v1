# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 00:09:08 2020

@author: apmle
"""

'''This is a code to calculate and display the fibonnaci structure'''

l=int(input("Please enter how long do you want your sequence to be.\n"))
sequence=[0,1]
i=0
while i <=l:
    seq= sequence[i]+sequence[i+1]
    sequence.append(seq)
    i+=1
print(f"the new fibonnaci sequence is ",end=' ')
print(*sequence)
            
            
            
            
            
            
            
            
            
            