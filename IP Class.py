# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:17:32 2020

@author: apmle
"""

''' This is a code to read the first eight numbers of IP address, 
in decimal format, and give the IP adress and informe what class they belong to
''' 
#Receive address
def class_ip(address):
    ip= address[:3] #same as [0:3] 0 to 3
    if int(ip) in range(0,127):
        print(f"The IP address {address} is class A")
    elif int(ip) in range(128,191):
        print(f"The IP address {address} is class B")    
    elif int(ip) in range(192,223):
        print(f"The IP address {address} is class C")
    elif int(ip) in range(224,239):
        print(f"The IP address {address} is class D")
    elif int(ip) > 240:
        print(f"The IP address {address} is class E")  


while True:
    add = input("Please type the IP adress of the computer using.\n")
    class_ip(add)
    cont=input("Do you wish to enter another IP address? If yes, type any key, or else type 0.\n")
    if cont =='0':
        break


