def maior_numero(numeros):
    numeros.sort()
    return numeros[-1]
print(maior_numero([1, 3, 4, 2, 5, 10, 6]))