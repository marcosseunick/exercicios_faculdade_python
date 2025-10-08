import gerenciador_json


ARQUIVO_EXERCICIOS = "db/exercicios.json"

def listar_exercicios():
    dados = gerenciador_json.carregar_dados_do_arquivo(ARQUIVO_EXERCICIOS)
    return dados

def adicionar_exercicio():
    pass

def buscar_exercicio_por_nome():
    pass

def remover_exercicio(id_do_exercicio):
    pass

def atualizar_exercicio(id_do_exercicio, novos_dados):
    lista_exercicios = gerenciador_json.carregar_dados_do_arquivo(ARQUIVO_EXERCICIOS)
    for exercicio in lista_exercicios:
        if id_do_exercicio["id"]:
            exercicio.update(novos_dados)
    gerenciador_json.salvar_dados_do_arquivo(ARQUIVO_EXERCICIOS, lista_exercicios)


