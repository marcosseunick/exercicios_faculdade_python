#Escreva um programa que exiba todos os divisores de um número fornecido pelo usuário.

numero = int(input("Digite um número inteiro positivo: "))

if numero <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    print(f"Os divisores de {numero} são:")
    for i in range(1, numero + 1):
        if numero % i == 0: 
            print(i)