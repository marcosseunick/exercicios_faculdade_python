# Crie um programa que leia vários números até que o usuário digite 0 e mostre a soma dos números lidos.

soma = 0
numero = 1 

while numero != 0:
    numero = int(input("Digite um número (digite 0 para sair): "))
    soma += numero

print(f"A soma dos números digitados é: {soma}")