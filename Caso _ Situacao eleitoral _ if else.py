# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 01:33:01 2020

@author: apmle
"""

# a primeira condicao/ if deve ser a que vai resolver a maior quantidade de problemas/ baseado nos dados
    #Exemplo
    #1. E obrigada a votar (18 <= idade<70)
    #2. Tem voto eletivo(16<=idade<=17  or idade >=70 )
    #3. Nao pode vota (idade<16)
    
def diagonosticar_situacao_eleitoral(idade):
    if idade >=18 and idade < 70:  # se eu nao adiciono 'and' ele pode escolher qualquer numero >18 like 7000 or any number<70.
        print("Tem dever de votar")
    elif idade < 16:
        print("Menor de idade; nao tem direito a voto")
    else:
        print("Voto facultativo") # se eu sempre que eu tiver n possibilidades, eu so preciso tratar n-1, ja que a ultima possibilidade e a que sobrar
            
diagonosticar_situacao_eleitoral(18)
diagonosticar_situacao_eleitoral(16) 
diagonosticar_situacao_eleitoral(80) 
diagonosticar_situacao_eleitoral(12)       
    
        