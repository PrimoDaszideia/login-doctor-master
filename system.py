#imports necessários do projeto

from unidades import unidadesEmails
import pandas as pd

logins_criados = []

#Entradas para busca da unidade

def buscar_unidade(entrada):
    for unidade in unidadesEmails:
        if (entrada.lower() in unidade["unidade"].lower() or
            entrada.lower() in unidade["email"].lower() or
            entrada.lower() in unidade["cnpj"].lower()):
            return unidade
    return None

#Sistema de autocomplementar e oferecer sugestões de possíveis unidades

def lista_de_sugeridas(texto):
    sugestoes = []

    for unidade in unidadesEmails:
        for valor in [unidade["unidade"], unidade["email"], unidade["cnpj"]]:
            if texto.lower() in valor.lower() and unidade["unidade"] not in sugestoes:
                sugestoes.append(unidade["unidade"])
    return sugestoes

#Formatação de nome

def formatar_nome(nome,titulo):

    if titulo.lower() in ["dr.","dra."]:
        return f"{nome} {titulo}"

    return nome 

#Gerar email

def gerador_de_email(nome,titulo,unidade_de_email):

    nome_formatado = "".join (nome.lower().split()) 
    prefixo =  titulo.lower(). replace(".","")

    return f"{prefixo}{nome_formatado}@{unidade_de_email}" 