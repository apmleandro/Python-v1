# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:48:50 2020

@author: apmle
"""

'''This is a code to calculate how many point will the robots in the competition 
will receive after trhowing the ball at a given distance from the hop '''


Dist=[]
Pontos=[]

while True:
    D=int(input("Please enter the distance between the robot and the hoop.\n"))
    Dist.append(D)
    if D<=0 or D >=2000 :
        print("Please enter a valid distance to the hoop")
    elif D<=800:
        point='1'
    elif D>800 and D<=1400:
        point='2'
        Pontos= Pontos.append(point)   
    elif D>1400 and D<=2000:
        point='3'
    Pontos.append(point)
    cont=input("Do you wish to enter another distance? Type any key for yes, or 0 for no.\n")
    if cont =='0':
        break


#    
#    
#    
print(f"{'Distancia':<30}\t{'Pontos':<30}")
print(f"{'=============================================================':^20}")

for d,y in zip(Dist,Pontos):
    print(f"{d:<30}\t|{point:<30}")
