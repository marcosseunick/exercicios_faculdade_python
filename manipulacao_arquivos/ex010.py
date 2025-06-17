# Mostrar Linhas com Palavra-Chave
# Crie uma função linhas_com_palavra(nome_arquivo, palavra) que retorne uma lista com as linhas do arquivo que contêm a palavra informada.

def linhas_com_palavra(nome_arquivo, palavra):
  with open(nome_arquivo, "r", encoding="UTF-8") as arquivo:
            linhas_encontradas = []
            for linha in arquivo:
                if palavra in linha:
                    linhas_encontradas.append(linha.strip())
                return linhas_encontradas
    