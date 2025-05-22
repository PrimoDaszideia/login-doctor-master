from tkinter import *
from tkinter import ttk
from tkinter import Tk
import tkinter as tk
from PIL import Image, ImageTk


# Janela pricipal
appMain = Tk()
appMain.title("Login Doctor Master")
appMain.iconbitmap("img/surgeon.ico")
appMain.geometry("800x450")

#Imagens do sistema

icone = Image.open("img/surgeon.png")       # Substitua pelo caminho da sua imagem
icone = icone.resize((24, 24))            # Redimensiona o ícone, se necessário
icone_tk = ImageTk.PhotoImage(icone)

# Seja Bem-Vindo
titulo = ttk.Label(appMain, text="Seja Bem-Vindo!", font=("Arial", 14))
titulo.pack(pady=10)


#entrada de nomes
title_name = ttk.Label(appMain, text="Nome do Especialista:")
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

#entrada de unidade + autocomplete

ttk.Label(appMain, text="Unidade:").pack()
entry_unidade = ttk.Entry(appMain, width= 35)
entry_unidade.pack(pady=1)


# Botões

planilha_unidade = tk.Button(appMain, text= "Listas de Login")
btn_login = tk.Button(appMain, image=icone_tk ,text="Ver Logins Criados", compound="left")
btn_login.pack(pady=5)
botao_image = icone_tk


appMain.mainloop()
