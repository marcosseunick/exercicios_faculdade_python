import json

def carregar_dados(caminho_do_arquivo):
    try:
        with open(caminho_do_arquivo, 'r', encoding = "utf-8") as arq:
                dados = json.load(arq)
        return dados
    except FileNotFoundError:
         return []


def salvar_dados(caminho_do_arquivo, dados_para_salvar):
        with open(caminho_do_arquivo, "w", encoding = "utf-8") as arq:
            dados = json.dump(dados_para_salvar, arq, indent = 4)
        return dados
