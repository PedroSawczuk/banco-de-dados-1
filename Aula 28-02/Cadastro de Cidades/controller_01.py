"""
Claudinei de Oliveira - encode: pt-br - utf-8 - data: 28-02-2023
controller.py
"""

from tkinter import messagebox
import re


def verifica_nomes(nomes):  
    if bool(re.search(r'\d', nomes)) == True or len(re.sub(r"\s+", "", nomes)) < 3:
        messagebox.showinfo(title = '', message = 'O Campo nome vazio, ou, com caracteres numéricos... ')
        return False
    else:
        return True
