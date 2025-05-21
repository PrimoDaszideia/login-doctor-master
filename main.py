from tkinter import *
from tkinter import ttk
from tkinter import Tk


# Janela pricipal
appMain = Tk()
appMain.title("Login Doctor Master")
appMain.iconbitmap("img/surgeon.ico")
appMain.geometry("800x450")

# Seja Bem-Vindo
titulo = ttk.Label(appMain, text="Seja Bem-Vindo!", font=("Arial", 14))
titulo.pack(pady=10)

#entrada de nomes
title_name = ttk.Label(appMain, text="Nome do Especialista")
title_name.pack(pady= 4)
entry_name = ttk.Entry(appMain, width= 35)
entry_name.pack(pady= 1)


#opções de login
'''title_opcoes = ["Dr." ,"Dra.","Recepcionista"]
opcoes_var = StringVar(value="Dr")
OptionMenu(appMain, opcoes_var, *title_opcoes)'''

#entrada de especialidade
ttk.Label(appMain, text= "Especialidade: ").pack()
entry_especialidade = Entry(appMain, width = 35)
entry_especialidade.pack()


# Botões
#btn_tabuada = tk.Button(janela, text="Tabuada", command=abrir_tabuada)
#btn_tabuada.pack(pady=5)


appMain.mainloop()
