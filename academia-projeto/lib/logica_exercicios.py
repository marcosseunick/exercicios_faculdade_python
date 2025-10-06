import gerenciador_json


ARQUIVO_EXERCICIOS = "db/exercicios.json"

def listar_exercicios():
    dados = gerenciador_json.carregar_dados_do_arquivo(ARQUIVO_EXERCICIOS)
    return dados
print(listar_exercicios())

def adicionar_exercicio():
    pass

def buscar_exercicio_por_nome():
    pass

def remover_exercicio(id_do_exercicio):
    pass

def atualizar_exercicio(id_do_exercicio, novos_dados):
    pass


