"""
Pedro Henrique Sawczuk Monteiro - encode: UTF8 - pt-br - data: 28-02-2023
sintese_1_scripts_28_02.py
"""

# 1 -  escrevendo em arquivo .csv a partir de uma lista

from csv import writer

with open('curso.csv', 'a') as arquivo:
    dados = writer(arquivo)
    curso = ''
    dados.writerow(['Curso', 'Disciplina', 'Carga_horaria'])
    while curso != 'sair':
        print()
        curso = input('Nome do curso ou sair para encerrar: ')
        if curso != 'sair':
            disciplina = input('\nNome da disciplina: ')
            carga_horaria = input('\nCarga horária semanal (em minutos) : ')
            dados.writerow([curso, disciplina, carga_horaria])


       
