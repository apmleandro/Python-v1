# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 23:47:51 2020

@author: apmle
"""

'''This is a code to calculate your Body Mass Index (BMI)'''
name=input("Please type you name and press enter\n")
def BMI_calc(name):
    while True:
        system = input("Please type of units would you like to use? US or SI?\n")
        system = system.upper()
        if system == 'US':
            
            print("What is your height?")
            
            feet = float(input("feet:    "))
            if feet == '0':
                print("Please enter a valid number")
            else:
                inches = float(input("inches:    "))
                if inches == '0':
                    print("Please enter a valid weight")
                else:
                    us_height= feet*12 +inches
                    us_weight=float(input("Please tell me your weight in lb.\n"))
                    if us_weight == '0':
                        print("Please enter a valid weight")
                    else:
                        BMI=round((703 * us_weight/us_height**2),2)
                        if BMI < 18.5:
                            print(f"Hello {name}! Your BMI is {BMI}. This means you are likely underweight. Please consut with your doctor.")
                        elif BMI >= 18.5 and BMI<=24.9:
                            print(f"Hello {name}! Your BMI is {BMI}. This means you are likely at normal weight.")
                        elif BMI >= 25 and BMI<=29.9:
                            print(f"Hello {name}! Your BMI is {BMI}. This means you are likely overweight. Please consult with your doctor.")
                        elif BMI >= 30:
                            print(f"Hello {name}! Your BMI is {BMI}. This means you are likely obese. Please consult with your doctor.")
    #                cont =input("Do you wish to repeat the test? If yes, press 1, if not press 0\n")
    #                if cont=='0':
    #                    break
                            
        elif system == 'SI':
        
            si_height =float(input("Please enter your height in meters\n"))
            
            if si_height == '0':
                print("Please enter a valid number")
            else:
                si_weight=float(input("Please tell me your weight in kg.\n"))
                if si_weight == '0':
                    print("Please enter a valid weight")
                else:
                    BMI=round(si_weight/(si_height**2),3)
                    if BMI < 18.5:
                        print(f"Hello {name}! Your BMI is {BMI}. This means you are likely underweight. Please consut with your doctor.")
                    elif BMI >= 18.5 and BMI<=24.9:
                        print(f"Hello {name}! Your BMI is {BMI}. This means you are likely at normal weight.")
                    elif BMI >= 25 and BMI<=29.9:
                        print(f"Hello {name}! Your BMI is {BMI}. This means you are likely overweight. Please consult with your doctor.")
                    elif BMI >= 30:
                        print(f"Hello {name}! Your BMI is {BMI}. This means you are likely obese. Please consult with your doctor.")
            
        else:
            print("Please enter a valid option")
        cont =input("Do you wish to repeat the test? If yes, press 1, if not press 0\n")
        if cont=='0':
            break
                            
        return BMI

BMI_calc(name)
        