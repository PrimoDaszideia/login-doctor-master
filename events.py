import tkinter as tk
from tkinter import messagebox, Toplevel, Text, Scrollbar, END, RIGHT, Y
from system import (
    criar_login,
    exportar_logins,
    exportar_unidades,
    copiar_logins,
    lista_de_sugeridas,
    logins_criados,
    excluir_logins
)

def event_adicionar(entry_name,entry_especialidade,entry_unidade,valor_inicial):

    nome = entry_name.get()
    especialidade = entry_especialidade.get()
    unidade = entry_unidade.get()
    prefixo = valor_inicial.get()
    resultado = criar_login(nome, especialidade, unidade, prefixo)

    if resultado["erro"]:
        messagebox.showerror("Erro", resultado["mensagem"])

    else:
        messagebox.showinfo("Login criado com sucesso!", resultado["mensagem"])

def event_exportar_login():
    
    resultado = exportar_logins()

    if resultado["erro"]:
        messagebox.showerror("Erro", resultado["mensagem"])

    else:
        messagebox.showinfo("Login exportado com sucesso!", resultado["mensagem"])

def event_unidade():

    resultado = exportar_unidades()

    if resultado["erro"]:
        messagebox.showerror("Erro", resultado["mensagem"])

    else:
        messagebox.showinfo("Unidade exportada com sucesso!", resultado["mensagem"])

def event_copiar():

    resultado = copiar_logins()

    if resultado["erro"]:
        messagebox.showerror("Erro", resultado["mensagem"])

    else:
        messagebox.showinfo("Copiado para a área de trasnferência!", resultado["mensagem"])

def event_autocompletar(entry_unidade,listbox_sugestoes):
    texto = entry_unidade.get()
    sugestoes = lista_de_sugeridas(texto)
    listbox_sugestoes.delete(0,tk.END)
    if sugestoes:
        for z in sugestoes:
            listbox_sugestoes.insert(tk.END, z)

        listbox_sugestoes.place(x = entry_unidade.winfo_x(), y = entry_unidade.winfo_y() + entry_unidade.winfo_height())
    else: 
        listbox_sugestoes.place_forget()

def event_selecionar(entry_unidades,listbox_sugestoes):

    selecao = listbox_sugestoes.get(tk.ANCHOR)
    entry_unidades.delete(0, tk.END)
    entry_unidades.insert(0, selecao)
    listbox_sugestoes.place_forget()

def event_excluir_logins(): 

    confirmacao = messagebox.askyesno("Deseja realmente excluir os logins?")
    if confirmacao: 
        resultado = excluir_logins()
        if resultado["erro"]:
            messagebox.showerror("Erro", resultado["mensagem"])

        else:
            messagebox.showinfo("Logins excluídos com sucesso.", resultado["mensagem"])
            