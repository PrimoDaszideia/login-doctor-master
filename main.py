import tkinter as tk
#from funcoes import gerar_tabuada  # Importa a função do outro arquivo

# Criar janela principal
janela = tk.Tk()
janela.title("Menu de Funções Matemáticas")
janela.geometry("300x300")

'''# Título
titulo = tk.Label(janela, text="Escolha uma funcionalidade:", font=("Arial", 14))
titulo.pack(pady=10)

# Botões
btn_tabuada = tk.Button(janela, text="Tabuada", command=abrir_tabuada)
btn_tabuada.pack(pady=5)

btn_conversor = tk.Button(janela, text="Conversor de Temperatura", command=abrir_conversor)
btn_conversor.pack(pady=5)

btn_calculadora = tk.Button(janela, text="Calculadora", command=abrir_calculadora)
btn_calculadora.pack(pady=5)

# Iniciar a interface'''
janela.mainloop()
