from itertools import combinations, permutations

def gerar_combinacoes(itens: list, k: int):

    lista_combinacoes = list(combinations(itens, k))
    contagem = len(lista_combinacoes)
    return lista_combinacoes, contagem

def gerar_arranjos(itens: list, k: int):

    lista_arranjos = list(permutations(itens, k))
    contagem = len(lista_arranjos)
    return lista_arranjos, contagem