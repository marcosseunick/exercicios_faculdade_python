#Crie um programa que leia 5 nomes e armazene em uma lista. Depois, exiba-os em ordem alfabética.

lista_nomes = []
for nome in range(1, 6):
    nomes = str(input("Digite um nome: "))
    lista_nomes.append(nomes)
print(lista_nomes)