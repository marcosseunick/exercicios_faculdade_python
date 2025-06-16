#solução com laço for:
def contar_linhas(nome_arquivo):
    with open(nome_arquivo, "r", encoding="UTF-8") as arquivo:
        total_linha = 0
        for linha in arquivo:
            total_linha += 1
    return total_linha


#solução com readlines()
def contar_linhas(nome_arquivo):
    with open(nome_arquivo, "r", encoding="UTF-8") as arquivo:
        contagem = arquivo.readlines()
        total_linha = len(contagem)
    return total_linha