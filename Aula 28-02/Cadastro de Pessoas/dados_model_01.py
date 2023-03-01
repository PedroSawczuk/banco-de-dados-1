"""
Pedro Henrique Sawczuk Monteiro - encode: UTF8 - pt-br - data: 28-02-2023
dados_model 
"""


def atualiza_lista(curso,  disciplina, carga_horaria, listas):
    listas.append([str(len(listas)),
                   curso.strip(),
                   disciplina.strip(),
                   carga_horaria.strip()])

   
def ler_arquivo(listas):
    try:
        with open('clientes.txt', 'r') as arquivo:
            conteudo = arquivo.readlines()
            [listas.append(i.split('|')) for i in conteudo]
    except FileNotFoundError:
        with open('clientes.txt', 'w') as arquivo:
            pass


def grava_no_arquivo(curso,  disciplina, carga_horaria, listas): 
    with open('clientes.txt', 'a') as arquivo:
        indice = str((len(listas)-1))
        arquivo.write('\n'+ indice +'|'+ curso + '|' + disciplina + '|' + carga_horaria)
    # from csv import writer
    # with open('curso.csv', 'a') as arquivo:
    #     dados = writer(arquivo)
    #     dados.writerow([curso, disciplina, carga_horaria])
