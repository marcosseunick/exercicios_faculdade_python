# Escreva um programa que conte quantos números entre 1 e 100 são pares.
contador = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        contador += 1
print(contador)