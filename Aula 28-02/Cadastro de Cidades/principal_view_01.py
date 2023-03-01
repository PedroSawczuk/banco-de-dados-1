"""
Claudinei de Oliveira - encode: UTF8 - pt-br - data: 28-02-2023
Refatorando para ler e escrever em arquivo.csv
"""

from tkinter import *  
from tkinter import ttk
from controller import *
from dados_model import *
import os

lista = [ ]

def valida_campos_digitados():
    
    valida = 1 if verifica_nomes(nome.get()) == True else 0
    
    if valida == 1:
        atualiza_lista(nome.get(), sobrenome.get(),lista)

        grava_no_arquivo(nome.get(), sobrenome.get(), lista)

        trvi.delete(*trvi.get_children())
        [trvi.insert("", "end", values=(c, r, n)) for (c, r, n) in lista]
        
        limpa_digitacao()
        messagebox.showinfo(title = '', message = 'Cliente cadastrado com sucesso... ')
        nome.focus_set()
          
 
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

lb_1 = Label(frame_1, text = 'Cadastro de endereço:',fg = '#FA0404', font=("Arial",14, "bold")).place(x = 15, y = 10, width = 200, height = 30)  
lb_2 = Label(frame_1, text = 'Cidade..........:', font=("Arial",12)).place(x = 15, y = 40, width = 112, height = 30)
lb_3 = Label(frame_1, text = 'Rua.:', font=("Arial",12)).place(x = 15, y = 80, width = 112, height = 30)
lb_4 = Label(frame_1, text = 'Número.:', font=("Arial",12)).place(x = 15, y = 120, width = 112, height = 30)

cidade = Entry(frame_1, relief = 'sunken', font=("Arial",12))
cidade.place(x = 115, y = 40, width = 550, height = 30)

rua = Entry(frame_1, relief = 'sunken', font=("Arial",12))
rua.place(x = 115, y = 80, width = 550, height = 30)

numero = Entry(frame_1, relief = 'sunken', font=("Arial",12))
numero.place(x = 115, y = 120, width = 550, height = 30)

trvi = ttk.Treeview(janela, columns = ('c', 'r', 'n'), show = 'headings')
nome.focus_set()

trvi.column('c', minwidth  = 0, width = 50)
trvi.column('r', minwidth = 0, width = 200)
trvi.column('n', minwidth  = 0, width = 200)

barra_vertical = Scrollbar(janela, orient='vertical', command=trvi.yview) 
trvi.configure(yscroll=barra_vertical.set)  
barra_vertical.pack(ipady=0, side = RIGHT)  

trvi.heading('id', text = 'Código')
trvi.heading('no', text = 'Nome')
trvi.heading('so', text = 'Sobrenome')

trvi.place(x = 10, y = 350, width = 1429, heigh = 425)

if len(lista) == 0:
    ler_arquivo(lista)
    [trvi.insert("", "end", values=(c, r, n)) for (c, r, n) in lista]

trvi.pack(ipadx=420, ipady=50, side = BOTTOM )  

btn_cadastra = Button(janela, text = 'Cadastrar', font=("Arial",12, "bold"), command = valida_campos_digitados)
btn_cadastra.place(x = 490, y = 300, width = 95, height = 40)

janela.mainloop()
