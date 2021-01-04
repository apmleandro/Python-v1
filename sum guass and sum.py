# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 02:51:15 2020

@author: apmle
"""

'''This is a code to calculate the sum of numbers between 1 and 100'''

n=int(input("Please enter last number of the sequence.\n"))
num=list(range(1,n+1,1))
soma=sum(num)
print(f"The sum of the numbers between 1 and 100 is {soma}")

#Gauss sum
#S=n((a1+an))/2
numbers=float(input("Please enter the number of terms in the serie.\n"))
a1=float(input("Please enter the first number of the series.\n"))
a2=float(input("Please enter the last number of the series.\n"))
soma_guass=n*(a1+a2)/2 #sum of a arithmetic sequence ( is a list of numbers with a definite pattern)
print(f"The sum of the numbers between 1 and 100 using guass method is {soma_guass}")
