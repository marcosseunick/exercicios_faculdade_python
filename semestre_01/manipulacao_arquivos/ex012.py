def ordenar_linhas(nome_arquivo_entrada, nome_arquivo_saida):
    linhas = []

    with open(nome_arquivo_entrada, "r", encoding="UTF-8") as arquivo_entrada:
            for linha in arquivo_entrada:
                linhas.append(linha.strip()) 


    linhas.sort()

    with open(nome_arquivo_saida, "w", encoding="UTF-8") as arquivo_saida:
            for linha_ordenada in linhas:
                arquivo_saida.write(linha_ordenada + "\n") 
