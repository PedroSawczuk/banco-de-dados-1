"""
Pedro Henrique Sawczuk Monteiro - encode: pt-br - utf-8 - data: 28-02-2023
controller.py
"""

from tkinter import messagebox
import re


def verifica_curso(curso):  
    if bool(re.search(r'\d', curso)) == True or len(re.sub(r"\s+", "", curso)) < 3:
        messagebox.showinfo(title = '', message = 'O campo CURSO vazio, ou, com caracteres numéricos... ')
        return False
    else:
        return True

def verifica_disciplina(disciplina):  
    if bool(re.search(r'\d', disciplina)) == True or len(re.sub(r"\s+", "", disciplina)) < 3:
        messagebox.showinfo(title = '', message = 'O campo DISCIPLINA vazio, ou, com caracteres numéricos... ')
        return False
    else:
        return True

# def verifica_carga_horaria(carga_horaria):  
#     cargas_horarias = int(carga_horaria)
#     if carga_horaria = 0: