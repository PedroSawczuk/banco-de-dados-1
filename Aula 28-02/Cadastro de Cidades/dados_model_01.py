"""
Professor: Claudinei de Oliveira - encode: UTF8 - pt-br - data: 28-02-2023
dados_model 
"""


def atualiza_lista(nomes, sobrenomes, listas):
    listas.append([str(len(listas)),
                   nomes.strip(),
                   sobrenomes.strip()])

   
def ler_arquivo(listas):
    try:
        with open('clientes.txt') as arquivo:
            conteudo = arquivo.readlines()
            [listas.append(i.split('|')) for i in conteudo]
    except FileNotFoundError:
        with open('clientes.txt', 'w') as arquivo:
            pass


def grava_no_arquivo(nomes, sobrenomes, listas): 
    with open('clientes.txt', 'a') as arquivo:
        indice = str((len(listas)-1))
        arquivo.write('\n'+indice+'|'+nomes+'|'+sobrenomes)
