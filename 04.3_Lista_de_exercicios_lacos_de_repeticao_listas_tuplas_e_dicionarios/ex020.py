#Leia uma lista de 10 números e exiba os números pares.

numeros = [1, 2, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)