def remover_palavra(nome_arquivo, palavra):
        with open(nome_arquivo, "r", encoding="UTF-8") as arquivo:
            conteudo = arquivo.read()

        novo_conteudo = conteudo.replace(palavra, "")

        with open(nome_arquivo, "w", encoding="UTF-8") as arquivo:
            arquivo.write(novo_conteudo)
