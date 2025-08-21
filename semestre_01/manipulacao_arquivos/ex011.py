def substituir_palavra(nome_arquivo, palavra_antiga, palavra_nova):
        with open(nome_arquivo, "r", encoding="UTF-8") as arquivo:
            conteudo = arquivo.read()

        novo_conteudo = conteudo.replace(palavra_antiga, palavra_nova)

        with open(nome_arquivo, "w", encoding="UTF-8") as arquivo:
            arquivo.write(novo_conteudo)