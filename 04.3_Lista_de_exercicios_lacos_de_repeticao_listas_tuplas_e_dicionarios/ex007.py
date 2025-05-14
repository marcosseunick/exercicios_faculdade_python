#Faça um programa que exiba todos os números ímpares de 1 até um número informado pelo usuário.

numero = int(input("Digite um número inteiro positivo: "))

print(f"Números ímpares de 1 até {numero}:")
for i in range(1, numero + 1, 2):
    print(i, end=' ')