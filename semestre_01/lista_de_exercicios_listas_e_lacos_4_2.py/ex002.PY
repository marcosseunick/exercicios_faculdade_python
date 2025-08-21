def somar_menores(lista):
    lista.sort()
    soma = lista[0] + lista[1]
    return soma

print(somar_menores([19, 5, 42, 2, 77]))
print(somar_menores([5, 8, 12, 18, 22]))
print(somar_menores([7, 15, 12, 18, 22]))
print(somar_menores([25, 42, 12, 18, 22]))
        