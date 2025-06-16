def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="UTF-8") as arquivo:
       leitura = arquivo.read()
    return leitura
