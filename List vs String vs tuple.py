# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:34:42 2020

@author: apmle
"""

x_list=[1,2,'Ana','Pedro']
x_tuple=(1,2,'Ana','Pedro')
x_string='Hello'


#I can concatanate on all of them

y_list= x_list +[1,2] # [1, 2, 'Ana', 'Pedro', 1, 2]
print(y_list)
y_tuple= x_tuple +(1,2) # (1, 2, 'Ana', 'Pedro', 1, 2)
print(y_tuple)
y_string=x_string + 'World' #'HelloWorld'
print(y_string)

#Can append on list

y_list.append(5) #[1, 2, 'Ana', 'Pedro', 1, 2, 5]
y_list.append('oi') #[1, 2, 'Ana', 'Pedro', 1, 2, 5, 'oi']
print(y_list)

#Can't append on string or tuple. It is not mutable!

y_tuple.append(5) 
y_tuple.append('oi')
print(y_tuple) #'tuple' object has no attribute 'append'


y_string.append(5) #[1, 2, 'Ana', 'Pedro', 1, 2, 5]
y_string.append('oi')
print(y_string) #AttributeError: 'str' object has no attribute 'append'


#Position 
y_list[2] #it's an element #'Ana'
y_string[2] # it's a substring # 'l'
y_tuple[2] # it's an element'Ana'



g=[(2,4), (5,7), (3,8), (5,9)] #--> This is a list of tuples
ylist = y_list+g #[1, 2, 'Ana', 'Pedro', 1, 2, 5, 'oi', (2, 4), (5, 7), (3, 8), (5, 9)]
y_list = y_list + g #[1, 2, 'Ana', 'Pedro', 1, 2, 5, 'oi', (2, 4), (5, 7), (3, 8), (5, 9)]

 
#String
x= "Por fim, nao tive filhos. \n Nao deixei a nenhum herdeiro o legado de nossa miseria."
# 'Por fim, nao tive filhos. \n Nao deixei a nenhum herdeiro o legado de nossa miseria.'

print(x) # quando uso print, ele sabe que \n e para pular uma linha
#Por fim, nao tive filhos. 
#Nao deixei a nenhum herdeiro o legado de nossa miseria.

x.splitlines() #Crio uma lista #cada elemento da lista e um "paragrafo"
#['Por fim, nao tive filhos. ', --> o primeiro elemento e tudo que eu tinha escrito na string antes de pular a primeira linha
# ' Nao deixei a nenhum herdeiro o legado de nossa miseria.']' --> O segundo elemento que tenho na string antes de pular 
#a segunda linha


