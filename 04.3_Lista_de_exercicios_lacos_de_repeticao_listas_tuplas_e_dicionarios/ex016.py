#Crie uma lista com 10 números digitados pelo usuário.
lista = []
for numeros in range(1, 11):
    numero = int(input("Digite um número: "))
    lista.append(numero)
print(lista)