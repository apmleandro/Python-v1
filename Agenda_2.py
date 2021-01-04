# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:39:27 2020

@author: apmle
"""

#Criar agenda de contatos

#1 passo criacao do menu de opcoes para a agenda

def exibir_menu():
     ''' Exibe o menu de opcoes do sistema.''' #---> string entre 3 aspas simples (''') e' usada para documentar o que faz uma funcao --> chamada doc spring
     print("Agenda de contatos")
     print("(1) Criar novo contato.")
     print("(2) Listar todos os contatos.")
     print("(3) Buscar um contato.")
     print("Selecione uma das opcoes acima.")
#Testar funcao --> doc spring    
exibir_menu()

#2abrir agenda em modo append

#criar funcao de cadastro


def cadastrar_contato(nome, telefone, email, arquivo_agenda='agenda.csv'): #se eu adicionar o nome da agenda de cara/o valor padrao do parametro, 
    
    agenda= open(arquivo_agenda, "a") #modo a vai adicionar o conteudo ao arquivo
    
    #escrevemos no arquivo:
    agenda.write(f"{nome},{telefone},{email}\n") #padrao americano separa por virgula 
    # fechar arquivo
    agenda.close()
    
    
    
cadastrar_contato("Grace hopper","+1 800 COBOL","ghoppers=@navy.mil")
cadastrar_contato("Ana Paula", "3077619014","guido@python.org")
cadastrar_contato("Margaret Hamilton", "+1 800 APOLLO", "mhamilton@nasa.gov")



def listar_contatos(arquivo_agenda): 
    ''' Lista nome, telefone e email de cada contato na agenda definida pelo caminho arquivo_agenda '''
    #Abre a agenda para leitura
    agenda =  open(arquivo_agenda, 'r') #read --> leitura e presumida se nao colocar 'r'

    contatos=agenda.read() #contatos e uma string sem separacao
   #fechar agenda
    agenda.close()
    contatos=contatos.splitlines() #contatos se torna uma lista--> cada linha(line) do arquivo e um elemento do contato agora e o contato inteiro. Por exemplo contato[0]=[nome1,telefone1,email1]
    print(f"{'Contato':<30}\t{'Telefone':>20}\t{'Email':<30}") #why to put in chaves se eles ja sao partes da string? Porque eu quero formatar ele
    print(f"{'=====================================================================================':^50}")
    
    for contato in contatos:  #contato e uma linha inteira da agenda
        contato=contato.split(',') #contato vai ser cada elemento present no i-term da lista contatos que vai ser separada por um character qualquer que eu escolher]
        print(contato)
        nome = contato[0]
        telefone = contato[1]
        email = contato[2]
        print(f"{nome:<30}\t|{telefone:>20}\t|{email:<30}")
        
        
listar_contatos('agenda.csv')


def buscar_contato(busca, arquivo_agenda): #definir termo de busca
    resultados = 0
    agenda =open(arquivo_agenda,'r')
    contatos = agenda.read()
    agenda.close()
    contatos = contatos.splitlines()
    for contato in contatos:
        contato = contato.split(',')# contato se torna uma lista com 3 elementos
        nome, telefone, email = contato[0], contato[1], contato[2]
        if busca.casefold() in nome.casefold() or busca.casefold() in telefone.casefold() or busca.casefold() in email.casefold():
            print(f"{nome:<30}\t|{telefone:>20}\t|{email:<30}")
            resultados += 1
    print(f"Encontrados(s) {resultados} resultados(s).")   

buscar_contato('Ana','agenda.csv')