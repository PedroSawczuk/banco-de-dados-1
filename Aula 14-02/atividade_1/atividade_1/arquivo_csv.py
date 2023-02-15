"""
Claudinei de Oliveira - encode: UTF8 - pt-br - data: 14-02-2023
arquivo_csv.py
 

# 1 -  Lendo arquivo .csv
with open("clientes.csv") as arquivo:
    dados = arquivo.read()
    print(type(dados))
    print(dados)


# 2 – Abrindo arquivo .csv no Python3 e  transformando os dados em lista
with open("clientes.csv") as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')
    print(dados)


# 3 – Abrindo arquivo.csv, transformando os dados em lista usando slice para retirar o cabeçalho
with open("clientes.csv") as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)
 

# 4 – Lendo arquivo.csv- módulo reader - cada linha será uma lista

from csv import reader

with open("clientes.csv") as arquivo: 
    dados = reader(arquivo)
    next(dados)  # pula a primeira lina onde está o cabeçalho
    for linha in dados:
        print(f'Nome: {linha[0]} - Sobrenome: {linha[1]} - Altura: {linha[2]}')
 

# 5 – Lendo arquivo.csv- método reader com separador ponto e vírgula
         # e caracteres especiais da língua portuguesa

from csv import reader

with open('clientes2.csv', encoding='utf-8') as arquivo:
    
    dados = reader(arquivo, delimiter=';')
    next(dados)  # ignora a primeira lina onde está o cabeçalho
    for linha in dados:
        print(f'Nome: {linha[0]} - Sobrenome: {linha[1]} - Altura: {linha[2]}')


# 6 –  DictReader lê o arquivo csv como ordered dicts, ou seja, como um dicionário

from csv import DictReader

with open('clientes.csv') as arquivo:
    dados = DictReader(arquivo)
    for linha in dados:  # cada linha será um orderect dic - dicionário
        print(f"{linha['Nome']} - {linha['sobrenome']} - {linha['altura (cm)']}")
"""

# 7 –  DictReader lê o arquivo csv como ordered dicts, ou seja, como um dicionário
          # com separador ponto e vírgula e caracteres especiais da língua portuguesa
          
from csv import DictReader

with open('clientes2.csv', encoding='utf-8') as arquivo:
    dados = DictReader(arquivo, delimiter=';') # cada linha será um orderect dic - dicionário
    for linha in dados:
        print(f"{linha['Nome']} - {linha['sobrenome']} - {linha['altura (cm)']}")   


