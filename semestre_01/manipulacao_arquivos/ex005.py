def contar_palavras(nome_arquivo):
    total = 0
    with open(nome_arquivo, "r", encoding="UTF-8") as arquivo:
        for linha in arquivo:
            palavras = linha.split()
            total += len(palavras)
