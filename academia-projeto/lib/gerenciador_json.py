import json
import os

def carregar_dados_do_arquivo(caminho_do_arquivo):
    try:
        with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)    
    except (FileNotFoundError):
        return []
    

def salvar_dados_do_arquivo(caminho_do_arquivo, dados_para_salvar):
    try:
        with open(caminho_do_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_para_salvar, arquivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erro ao salvar o aquivo {caminho_do_arquivo} : {e}")
        return False
    
    
CAMINHO_EXERCICIOS = 'db/exercicios.json'
CAMINHO_TREINOS = 'db/treinos.json'

def carregar_exercicios(caminho_do_arquivo):
    return carregar_dados_do_arquivo(CAMINHO_EXERCICIOS)

def salvar_exercicios(lista_exercicios):
    return salvar_dados_do_arquivo(CAMINHO_EXERCICIOS, lista_exercicios)

def carregar_treinos():
    return carregar_dados_do_arquivo(CAMINHO_TREINOS)

def salvar_treinos(lista_treinos):
    return salvar_dados_do_arquivo(CAMINHO_TREINOS, lista_treinos)