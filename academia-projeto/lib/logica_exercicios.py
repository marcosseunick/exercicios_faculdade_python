import gerenciador_json

ARQUIVO_EXERCICIOS = "db/exercicios.json"

def listar_exercicios():
    dados = gerenciador_json.carregar_dados(ARQUIVO_EXERCICIOS)
    return dados