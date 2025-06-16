def adicionar_linha(nome_arquivo, linha):
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()

    conteudo += "\n" + linha

    with open(nome_arquivo, "w", encoding="UTF-8") as arq:
        arq.write(conteudo)
