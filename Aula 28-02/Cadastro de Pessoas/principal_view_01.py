"""
Pedro Henrique Sawczuk Monteiro - encode: UTF8 - pt-br - data: 28-02-2023
Refatorando para ler e escrever em arquivo.csv
"""

from tkinter import *  
from tkinter import ttk
from controller_01 import *
from dados_model_01 import *
import os

lista = [ ]

def valida_campos_digitados():
    
    valida = 1 if verifica_curso(curso.get()) == True else 0
    valida = 2 if verifica_disciplina(disciplina.get()) == True else 0
    # valida = 3 if verifica_carga_horaria(carga_horaria.get()) == True else 0
    
    if valida == 2:
        atualiza_lista(curso.get(), disciplina.get(), carga_horaria.get(), lista)

        grava_no_arquivo(curso.get(), disciplina.get(), carga_horaria.get(),  lista)

        trvi.delete(*trvi.get_children())
        [trvi.insert("", "end", values=(i, c, d, h)) for (i, c, d, h) in lista]
        
        limpa_digitacao()
        messagebox.showinfo(title = '', message = 'Curso cadastrado com sucesso... ')
        curso.focus_set()
          
 
def destroi_frame_1():
        for widget in frame_1.winfo_children():
            widget.destroy()

            
def limpa_digitacao():
    curso.delete(0,END), disciplina.delete(0,END), carga_horaria.delete(0,END)


janela =  Tk()
janela.title('Curso de Analise e desenvolvimento de Software - IFRO')

janela.geometry('1435x890+0+0') 
janela.configure(background = '#F8F8FF')  
janela.resizable(True, True)  

frame_1 = Frame(janela, borderwidth = 1, relief = 'solid')
frame_1.place(x = 3, y = 3, width = 1429, heigh = 290)

lb_1 = Label(frame_1, text = 'Cadastro de curso:',fg = '#FA0404', font=("Arial",14, "bold")).place(x = 15, y = 10, width = 200, height = 30)  
lb_2 = Label(frame_1, text = 'Nome do Curso..........:', font=("Arial",12)).place(x = 20, y = 40, width = 170, height = 30)
lb_3 = Label(frame_1, text = 'Disciplina.:', font=("Arial",12)).place(x = 15, y = 80, width = 170, height = 30)
lb_4 = Label(frame_1, text = 'Carga Horária.:', font=("Arial",12)).place(x = 10, y = 120, width = 170, height = 30)

curso = Entry(frame_1, relief = 'sunken', font=("Arial",12))
curso.place(x = 205, y = 40, width = 550, height = 30)

disciplina = Entry(frame_1, relief = 'sunken', font=("Arial",12))
disciplina.place(x = 140, y = 80, width = 300, height = 30)

carga_horaria = Entry(frame_1, relief = 'sunken', font=("Arial",12))
carga_horaria.place(x = 140, y = 120, width = 300, height = 30)

trvi = ttk.Treeview(janela, columns = ('id', 'cr', 'di', 'ch'), show = 'headings')
curso.focus_set()

trvi.column('id', minwidth  = 0, width = 50)
trvi.column('cr', minwidth = 0, width = 200)
trvi.column('di', minwidth  = 0, width = 200)
trvi.column('ch', minwidth  = 0, width = 200)

barra_vertical = Scrollbar(janela, orient='vertical', command=trvi.yview) 
trvi.configure(yscroll=barra_vertical.set)  
barra_vertical.pack(ipady=0, side = RIGHT)  

trvi.heading('id', text = 'Código')
trvi.heading('cr', text = 'Curso')
trvi.heading('di', text = 'Disciplina')
trvi.heading('ch', text = 'Carga Horária')

trvi.place(x = 10, y = 350, width = 1429, heigh = 425)

if len(lista) == 0:
    ler_arquivo(lista)
    [trvi.insert("", "end", values=(i, c, d, h)) for (i, c, d, h) in lista]

trvi.pack(ipadx=420, ipady=50, side = BOTTOM )  

btn_cadastra = Button(janela, text = 'Cadastrar', font=("Arial",12, "bold"), command = valida_campos_digitados)
btn_cadastra.place(x = 490, y = 300, width = 95, height = 40)

janela.mainloop()
