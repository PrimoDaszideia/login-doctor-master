#imports necessários do projeto

from unidades import unidadesEmails
import pandas as pd
import pyperclip

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

#Gerador de senha

def gerador_de_senha(email):

    return email.split("@")[0]

#Criador de login

def criar_login(nome,especialidade,nome_de_unidade,titulo):

    unidade = buscar_unidade(nome_de_unidade)
    if not unidade: 
        return {"erro": True, "mensagem":"unidade não encontrada"}  

    nome_formatado = formatar_nome(titulo,nome)
    email = gerador_de_email(titulo,nome,unidade["email"])
    senha = gerador_de_senha(email)

    dados_do_login = {

     "nome": nome_formatado,
     "especialidade": especialidade,
     "unidade": unidade["unidade"],
     "email": email,
     "senha": senha
    }

    logins_criados.append(dados_do_login)

    mensagem = f"""

    Nome: {nome_formatado}
    Especialidade: {especialidade}
    Unidade: {unidade['unidade']}
    Email: {email}
    Senha: {senha}

    """
    return {"erro": False, "mensagem": mensagem.strip()} 

#Exportar do excel

def exportar_logins(nome_de_arquivo = "logins.xlsx"):
    if not logins_criados:
        return {"erro": True, "mensagem": "Nenhum login criado."}

    df = pd.DataFrame(logins_criados) 
    df.to_excel(nome_de_arquivo, index= False)

    return {"erro": False, "mensagem": "Arquivo salvo com sucesso."}

def exportar_unidades(nome_de_arquivo = "unidades.xlsx"):

    df = pd.DataFrame(unidadesEmails) 
    df.to_excel(nome_de_arquivo, index= False)

    return {"erro": False, "mensagem": "Arquivo salvo com sucesso."}

#Copiar para a área de transferência

def copiar_logins():
    if not logins_criados:
        return {"erro": True, "mensagem": "Nada para copiar."}

    texto = "" 


    for login in logins_criados: 
        texto += f"{login['nome']} / {login['email']} / {login['senha']} \n" 

    pyperclip.copy(texto.strip())

    return {"erro": False, "mensagem": "Logins copiados para a área de transferência."}
