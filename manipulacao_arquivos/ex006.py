def copiar_arquivo(origem, destino):
        with open(origem, "r") as arquivo_origem:
            conteudo = arquivo_origem.read()
        with open(destino, "w") as arquivo_destino:
            arquivo_destino.write(conteudo)
        return True
