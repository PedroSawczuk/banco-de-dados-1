"""
Acadêmico(a):       - encode: UTF8 - pt-br - data: 14-02-2023
Manipulando dados
dados_model.py 
"""

def atualiza_lista(nomes, sobrenomes, listas):
    listas.append([str(len(listas)),
                   nomes.strip(),
                   sobrenomes.strip()])

   
def ler_arquivo(listas):

    from csv import reader

    with open('clientes.csv') as arquivo:
        dados = reader(arquivo, delimiter=';')
        next(dados)  # pula a primeira lina onde está o cabeçalho
        dados = arquivo.readline

# def ler_arquivo(listas):
#     try:
#         with open('clientes.txt') as arquivo:
#             conteudo = arquivo.readlines()
#             [listas.append(i.split('|')) for i in conteudo]
#     except FileNotFoundError:
#         with open('clientes.txt', 'w') as arquivo:
#             pass

