import gerenciador_json
import pandas as pd
import os
import json

ARQUIVO_EXERCICIOS = "db/exercicios.json"

def listar_exercicios():
    dados = gerenciador_json.carregar_dados_do_arquivo(ARQUIVO_EXERCICIOS)
    return dados

def adicionar_exercicio():
    print("\n--- ADICIONAR NOVO Exercicio ---")
    
    pessoa = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    nome = input("Digite o nome do novo exercicio: ")
    tipo = input("Digite o tipo do novo exercicio: ")
    repeticoes = int(input("Digite a quantidadade de repeticoes do novo exercicio: "))
    df = ler_dados()
    if not df.empty and 'id' in df.columns and pd.notna(df['id']).any():
        novo_id = df['id'].max() + 1
    else:
        novo_id = 1

    novo_exercicio = {'id': novo_id, 'nome': pessoa, "idade": idade,'exercicio': nome, 'tipo': tipo, 'repeticao': repeticoes}
    df_novo_exercicio = pd.DataFrame([novo_exercicio])
    df_atualizado = pd.concat([df, df_novo_exercicio], ignore_index=True)
    salvar_dados(df_atualizado)
    
    return df_atualizado
def ler_dados() -> pd.DataFrame:
    CHAVE_PRINCIPAL = 'exercicios'
    try:
        
        if not os.path.exists(ARQUIVO_EXERCICIOS):
            return pd.DataFrame(columns=['id', 'nome', 'tipo', 'quantidade'], dtype=object)
        with open(ARQUIVO_EXERCICIOS, 'r') as f:
            dados_json = json.load(f)
        df = pd.json_normalize(dados_json[CHAVE_PRINCIPAL])
        if not df.empty and 'id' in df.columns:
            df['id'] = pd.to_numeric(df['id'], errors='coerce').astype('Int64') 
        return df
    
    
    except KeyError:
        print(f"ERRO: Chave '{CHAVE_PRINCIPAL}' não encontrada no JSON. Retornando DF vazio.")
        return pd.DataFrame(columns=['id', 'nome', 'idade'], dtype=object)
    
    except Exception as e:
        print(f"ERRO de Leitura: Não foi possível processar o JSON. Detalhes: {e}")
        return pd.DataFrame(columns=['id', 'nome', 'idade'], dtype=object)

def salvar_dados(df: pd.DataFrame):
    CHAVE_PRINCIPAL = 'exercicios'
    try:
    
        dados_lista = df.to_dict(orient='records')
        dados_para_salvar = {
            CHAVE_PRINCIPAL: dados_lista
        }
        os.makedirs(os.path.dirname(ARQUIVO_EXERCICIOS), exist_ok=True)
        with open(ARQUIVO_EXERCICIOS, 'w') as f:
            json.dump(dados_para_salvar, f, indent=4)
            
        print(f"\n[SUCESSO] Dados salvos e arquivo atualizado em {ARQUIVO_EXERCICIOS}.")
    except Exception as e:
        print(f"\n[ERRO] de Escrita: Não foi possível salvar o arquivo. Detalhes: {e}")

def buscar_exercicio_por_nome(nome_pesquisado):
    pass

def remover_exercicio(id_do_exercicio):
    listar_exercicios = gerenciador_json.carregar_dados_do_arquivo(ARQUIVO_EXERCICIOS)

    tamanho_original = len(listar_exercicios)

    nova_lista_exercicios = [
        exercicio for exercicio in listar_exercicios
        if exercicio.get("id") != id_do_exercicio
    ]

    if len(nova_lista_exercicios) < tamanho_original:
        gerenciador_json.salvar_dados_do_arquivo(ARQUIVO_EXERCICIOS, nova_lista_exercicios)
        return True
    return False

def atualizar_exercicio(id_do_exercicio, novos_dados):
    lista_exercicios = gerenciador_json.carregar_dados_do_arquivo(ARQUIVO_EXERCICIOS)
    for exercicio in lista_exercicios:
        if id_do_exercicio == exercicio["id"]:
            exercicio.update(novos_dados)
            break
    gerenciador_json.salvar_dados_do_arquivo(ARQUIVO_EXERCICIOS, lista_exercicios)
