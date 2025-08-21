# 14 - Elabore um algoritmo que recebe 05 bits individualmente de um número binário e mostre o número decimal.

bit1 = int(input("Digite o primeiro bit (0 ou 1): "))
bit2 = int(input("Digite o segundo bit (0 ou 1): "))
bit3 = int(input("Digite o terceiro bit (0 ou 1): "))
bit4 = int(input("Digite o quarto bit (0 ou 1): "))
bit5 = int(input("Digite o quinto bit (0 ou 1): "))

if (bit1 in {0, 1} and bit2 in {0, 1} and bit3 in {0, 1} and bit4 in {0, 1} and bit5 in {0, 1}):
  binario = f"{bit1}{bit2}{bit3}{bit4}{bit5}"
  decimal = 0
  for i in range(5):
    bit = int(binario[i])
    potencia = 4 - i
    decimal += bit * (2**potencia)
  print(f"O número binário {binario} em decimal é: {decimal}")
else:
  print("Por favor, insira apenas bits válidos (0 ou 1).")