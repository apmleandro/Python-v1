# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:25:07 2020

@author: apmle
"""

'''This is a code to read a character and inform whether it is a vowel or a consonant'''
while True:
    letter=input("Please enter a letter.\n")
    #letter= letter.lower()
    letter=letter.casefold()
    vowel=['a','e','i','o','u']
    if letter in vowel:
        print(f"The letter {letter} is a vowel.\n")
    else:
        print(f"The letter {letter} is a consonant.\n")
    cont=(input("Do you wish to enter another vowel? If yes type any key, if no, press 0.\n"))
    if cont == '0':
        break   
    
    
    
    


