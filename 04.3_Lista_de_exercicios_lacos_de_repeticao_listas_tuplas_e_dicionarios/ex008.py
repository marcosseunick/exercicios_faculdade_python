# Escreva um código que solicite nomes até que a palavra "fim" seja digitada, e depois exiba todos os nomes digitados.

lista_nomes = []
while True:
    nome = input("Digite um nome: ")
    if nome == "fim":
        break
    lista_nomes.append(nome)
print(lista_nomes)