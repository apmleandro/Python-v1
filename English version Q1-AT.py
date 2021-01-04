# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:40:19 2020

@author: apmle
"""


import matplotlib.pyplot as plt



def get_data():
    while True:
        try:
            Val=int(input("Please tell me how much money do you have currently:\n$"))
            if Val<0:
                print("Please type a value higher than 0")
                continue
        except ValueError:
            print("Sorry, I didn't understand that! Please type a value higher than $0,00.")
            continue
        else:
            break
    
    while True:
        try:
            Rend=float(input("Please tell us the monthly interest you are planning to earn:\n"))
            if Rend<0:
                print("Please type a value higher than 0")
                continue
        except ValueError:
            print("Sorry, I didn't understand that! Please type a value higher than 0,00.")
            continue
        else:
            break
    
    while True:
        try:
            Aporte=int(input("Please tell me how much you wil deposit monthly.\nR$"))
            if Aporte<0:
                print("Please type a value higher than 0")
                continue
        except ValueError:
            print("Sorry, I didn't understand that! Please type a value higher than 0,00.")
            continue
        else:
            break
    
    while True:
        try:
            meses=int(input("Please tell me how many months do you wish to save?\n"))
            if meses<0:
                print("Please type a value higher than 0")
                continue
        except ValueError:
            print("Sorry, I didn't undersand that. Please type a number higher than 0.")
            continue
        else:
            break
    
    return Val,Rend,Aporte,meses


def calc_einstein(Val,Rend,Aporte,meses):
    valor_mes=[]
    i=0
    while i<meses:
            Val=Val+Val*(Rend/100)
            Val=round(Val+Aporte,2)
            valor_mes.append(Val)
            print(f"(After {i+1} months(s), the amount of money you will have is {valor_mes[i]}.")
            i+=1
                        

    return valor_mes

#running program
v,r,a,m=get_data()   
values=calc_einstein(v,r,a,m)

months=[]

for x in range(m):
    months.append(x+1)

#Plotting data


plt.plot(months,values,'r')
plt.xlabel('Months')
plt.ylabel('Money earned')
plt.title('Money Progession')
plt.legend("A1")
plt.show()

