#Faça um programa que leia um número e exiba sua tabuada de multiplicação (1 a 10).

numero = int(input("Digite um número para saber a tabuada: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado * i}")