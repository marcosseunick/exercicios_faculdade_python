def escrever_texto(nome_arquivo, texto):
    with open(nome_arquivo, "w", encoding="UTF-8") as arquivo:
      arquivo.write(texto) 

    