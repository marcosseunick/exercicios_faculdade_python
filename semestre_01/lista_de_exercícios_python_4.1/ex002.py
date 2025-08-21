# 2. Faça um algoritmo que receba um binário e converta o valor em um número inteiro

binario = input("Digite um número binário: ")

resultado_inteiro = 0
comprimento = len(binario)

for i in range(comprimento):
    digito = int(binario[i])
    potencia = comprimento - i - 1
    resultado_inteiro += digito * (2 ** potencia)

print(f"O valor inteiro de {binario} é: {resultado_inteiro}")
  