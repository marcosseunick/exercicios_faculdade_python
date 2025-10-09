import json
import os

def carregar_dados_do_arquivo(caminho_do_arquivo):
    try:
        with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)    
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    

def salvar_dados_do_arquivo(caminho_do_arquivo, dados_para_salvar):
    try:
        with open(caminho_do_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_para_salvar, arquivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erro ao salvar o aquivo {caminho_do_arquivo} : {e}")
        return False
    

