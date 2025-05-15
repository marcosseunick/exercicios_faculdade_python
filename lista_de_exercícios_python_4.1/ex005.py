# Dado uma matriz de inteiros, encontre o elemento que aparece com mais frequência na matriz. Se houver vários
# elementos com a mesma frequência máxima, retorne qualquer um deles.

matriz = [
    [0, 1, 2],
    [3, 5, 10],
    [10, 14, 30]
]


lista_unica = []
for linha in matriz:
    lista_unica.extend(linha)


contagem = {}
for num in lista_unica:
    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1


elemento_mais_frequente = max(contagem, key=contagem.get)
print(elemento_mais_frequente)