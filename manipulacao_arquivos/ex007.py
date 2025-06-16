def exibir_com_numeracao(nome_arquivo):
    with open(nome_arquivo, "r", encoding="UTF-8") as arquivo:
        linhas = arquivo.readlines()

    for numero, linha in enumerate(linhas, start=1):
        linha_limpa = linha.rstrip()
        print(f"{numero}: {linha_limpa}")