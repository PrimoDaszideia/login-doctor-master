from tkinter import *
from tkinter import ttk
from tkinter import Tk
import tkinter as tk
from events import *
from PIL import Image, ImageTk
from system import *


# Janela pricipal
appMain = Tk()
appMain.title("Login Doctor Master")
appMain.iconbitmap("img/surgeon.ico")
appMain.geometry("800x450")

#Imagens do sistema

icone = Image.open("img/surgeon.png")       # Substitua pelo caminho da sua imagem
icone = icone.resize((24, 24))            # Redimensiona o ícone, se necessário
icone_tk = ImageTk.PhotoImage(icone)
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

ttk.Label(appMain, text="Unidade:").pack()
entry_unidade = ttk.Entry(appMain, width= 35)
entry_unidade.pack(pady=1)


# Botões

bnt_adicionar = tk.Button(appMain, image= adicionar_login_tk ,text = " Adicionar Login", compound="left")
bnt_adicionar.pack(pady=5)
bnt_adicionar = adicionar_login_tk
bnt_unidade = tk.Button(appMain, image= excel_tk,text= " Exportar Unidades", compound="left",command=exportar_unidades)
bnt_unidade.pack(pady=5)
bnt_unidade = excel_tk
btn_login = tk.Button(appMain, image=icone_tk ,text="Ver Logins", compound="left")
btn_login.pack(pady=5)
botao_image = icone_tk
bnt_export_login = tk.Button(appMain, text = 'Exportar Login', command= exportar_logins)
bnt_export_login.pack(pady=5)


appMain.mainloop()
