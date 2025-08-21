#Solicite 10 números ao usuário e exiba a média aritmética.

lista = []
for i in range(10):
    numeros = int(input("Digite um número: "))
    lista.append(numeros)
media = sum(lista) / len(lista)
print(media)