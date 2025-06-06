from tkinter import *
from tkinter import ttk
from tkinter import Tk
import tkinter as tk
from events import (event_unidade,event_selecionar,event_adicionar,event_autocompletar,event_copiar,event_exportar_login,event_excluir_logins)
from PIL import Image, ImageTk
from system import *


# Janela pricipal
appMain = Tk()
appMain.title("Login Doctor Master")
appMain.iconbitmap("img/surgeon.ico")
appMain.geometry("800x450")

#Imagens do sistema
ver_login = Image.open("img/eye.png")       # Substitua pelo caminho da sua imagem
ver_login = ver_login.resize((24, 24))            # Redimensiona o ícone, se necessário
ver_login_tk = ImageTk.PhotoImage(ver_login)

excluir = Image.open("img/remover-usuario.png")
excluir = excluir.resize((24,24))
excluir_tk = ImageTk.PhotoImage(excluir)

baixar_login = Image.open("img/download.png")
baixar_login = baixar_login.resize((24, 24))
baixar_login_tk = ImageTk.PhotoImage(baixar_login)

copiar = Image.open("img/copiando.png")
copiar = copiar.resize((24,24))
copiar_tk = ImageTk.PhotoImage(copiar)

excel = Image.open('img/extensao-de-formato-de-arquivo-xlsx.png')
excel = excel.resize((24,24))
excel_tk = ImageTk.PhotoImage(excel)

adicionar_login = Image.open('img/adicionar-usuario.png')
adicionar_login = adicionar_login.resize((24,24))
adicionar_login_tk = ImageTk.PhotoImage(adicionar_login)

# Seja Bem-Vindo
titulo = ttk.Label(appMain, text="Seja Bem-Vindo!", font=("Arial", 14))
titulo.pack(pady=10)

#Escolha de Prefixo

prefixo_opcoes = ["Dr." ,"Dra.","Recepcionista"]
valor_inicial = tk.StringVar(value=prefixo_opcoes[0])
OptionMenu(appMain, valor_inicial, *prefixo_opcoes)
menu_option = tk.OptionMenu(appMain, valor_inicial, *prefixo_opcoes)
menu_option.pack(pady=10)
menu_option.pack(padx=10)

#entrada de nomes
title_name = ttk.Label(appMain, text="Nome do Especialista:")
title_name.pack(pady= 4)
entry_name = ttk.Entry(appMain, width= 35)
entry_name.pack(pady= 1)

#entrada de especialidade
ttk.Label(appMain, text= "Especialidade: ").pack()
entry_especialidade = Entry(appMain, width = 35)
entry_especialidade.pack()

#entrada de unidade + autocomplete

unidade = tk.Label(appMain, text="Unidade").pack()
entry_unidade = ttk.Entry(appMain, width= 35)
entry_unidade.pack(pady=1)

listbox_sugestoes = Listbox(appMain, height=4, width= 35)
listbox_sugestoes.place_forget()
entry_unidade.bind("<KeyRelease>", lambda e: event_autocompletar(entry_unidade, listbox_sugestoes))
listbox_sugestoes.bind("<ButtonRelease-1>", lambda e: event_selecionar(entry_unidade, listbox_sugestoes))

# Botões

#botão de adicionar
bnt_adicionar = tk.Button(appMain, 
    image= adicionar_login_tk ,
    text = " Adicionar Login", 
    compound="left", 
    command=lambda: event_adicionar(entry_name,entry_especialidade,entry_unidade,valor_inicial)
)
bnt_adicionar.pack(side= tk.LEFT, padx = (40,5))

#botão de excluir logins
bnt_excluir_logins = tk.Button(appMain, image= excluir_tk,  text= "Excluir Logins", compound="left", command=lambda:event_excluir_logins)
bnt_excluir_logins.pack(side= tk.LEFT, padx = 5)

#botão de ver login
btn_ver_login = tk.Button(appMain, image=ver_login_tk ,text="Ver Logins", compound="left")
btn_ver_login.pack(side= tk.LEFT, padx= 5)

#botão de copiar login
bnt_copiar_login = tk.Button(appMain, 
    image=copiar_tk ,text = 
    'Copiar Logins', 
    compound="left" ,
    command= lambda: event_copiar()
                             
)
bnt_copiar_login.pack(side= tk.LEFT, padx= 5)

#botão de baixar login para xlsx
bnt_baixar_login = tk.Button(appMain, 
    image= baixar_login_tk, 
    text = 'Exportar Logins', 
    compound= "left", 
    command= lambda: event_exportar_login()
)
bnt_baixar_login.pack(side= tk.LEFT, padx= 5)

#botão de exportar unidades para xlsx
bnt_unidade = tk.Button(appMain, 
    image= excel_tk,
    text= " Exportar Unidades", 
    compound="left",
    command= lambda: event_unidade()
)
bnt_unidade.pack(side= tk.LEFT, padx= 5)



appMain.mainloop()
