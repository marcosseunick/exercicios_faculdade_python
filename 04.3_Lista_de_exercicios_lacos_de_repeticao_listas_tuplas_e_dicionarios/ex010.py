#Escreva um programa que calcule o fatorial de um número usando laço for.

numero = int(input("Digite um número inteiro não negativo: "))
fatorial = 1

if numero < 0:
    print("O fatorial não está definido para números negativos.")
else:
    for i in range(1, numero + 1):
        fatorial *= i 
    print(f"O fatorial de {numero} é {fatorial}.")
    