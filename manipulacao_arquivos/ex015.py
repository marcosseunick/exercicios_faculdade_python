def inverter_linhas(nome_arquivo_entrada, nome_arquivo_saida):
        with open(nome_arquivo_entrada, "r", encoding="UTF-8") as arquivo_entrada:
            linhas = arquivo_entrada.readlines()

        linhas_invertidas = linhas[::-1]

        with open(nome_arquivo_saida, "w", encoding="UTF-8") as arquivo_saida:
            arquivo_saida.writelines(linhas_invertidas)

        print(f"A ordem das linhas de '{nome_arquivo_entrada}' foi invertida e salva em '{nome_arquivo_saida}'.")