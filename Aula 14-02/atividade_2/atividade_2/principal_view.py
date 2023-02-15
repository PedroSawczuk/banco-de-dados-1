"""
Claudinei de Oliveira - encode: UTF8 - pt-br - data: 14-02-2022
Tkinter - Manipulando arquivos
principal_view.py
"""

from tkinter import *  
from tkinter import ttk
from dados_model import *
import os

lista = [ ]

 
def destroi_frame_1():
        for widget in frame_1.winfo_children():
            widget.destroy()

            
def limpa_digitacao():
    nome.delete(0,END), sobrenome.delete(0,END)


janela =  Tk()
janela.title('Curso de Analise e desenvolvimento de Software - IFRO')

janela.geometry('1435x890+0+0') 
janela.configure(background = '#F8F8FF')  
janela.resizable(True, True)  

frame_1 = Frame(janela, borderwidth = 1, relief = 'solid')
frame_1.place(x = 3, y = 3, width = 1429, heigh = 290)

lb_1 = Label(frame_1, text = ' de usuários:',fg = '#FA0404', font=("Arial",14, "bold")).place(x = 15, y = 10, width = 200, height = 30)  
lb_2 = Label(frame_1, text = 'Nome..........:', font=("Arial",12)).place(x = 15, y = 40, width = 112, height = 30)
lb_3 = Label(frame_1, text = 'Sobrenome.:', font=("Arial",12)).place(x = 15, y = 80, width = 112, height = 30)
lb_4 = Label(frame_1, text = 'Altura.:', font=("Arial",12)).place(x = 15, y = 120, width = 112, height = 30)

nome = Entry(frame_1, relief = 'sunken', font=("Arial",12))
nome.place(x = 115, y = 40, width = 550, height = 30)

sobrenome = Entry(frame_1, relief = 'sunken', font=("Arial",12))
sobrenome.place(x = 115, y = 80, width = 300, height = 30)

altura = Entry(frame_1, relief = 'sunken', font=("Arial",12))
altura.place(x = 115, y = 120, width = 300, height = 30)

trvi = ttk.Treeview(janela, columns = ('no', 'so', 'al'), show = 'headings')
nome.focus_set()

trvi.column('no', minwidth  = 0, width = 200)
trvi.column('so', minwidth = 0, width = 200)
trvi.column('al', minwidth  = 0, width = 200)

barra_vertical = Scrollbar(janela, orient='vertical', command=trvi.yview) # cria
trvi.configure(yscroll=barra_vertical.set) # configura
barra_vertical.pack(ipady=0, side = RIGHT) # posiciona

trvi.heading('no', text = 'NOME')
trvi.heading('so', text = 'SOBRENOME')
trvi.heading('al', text = 'ALTURA')

if len(lista) == 0:
    ler_arquivo(lista)
    [trvi.insert("", "end", values=(n, s, a)) for (n, s, a) in lista]

trvi.place(x = 10, y = 350, width = 1429, heigh = 425)
trvi.pack(ipadx=420, ipady=50, side = BOTTOM ) # apresenta barra de rolagem na tela

janela.mainloop()
