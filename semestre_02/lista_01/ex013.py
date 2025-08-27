# Função resto_divisao()
# Peça dois números e mostre o resto da divisão do primeiro pelo segundo.

def resto_divisao():

  dividendo = int(input("Digite o número que será dividido: "))
  divisor = int(input("Digite o número divisor: "))

  resto = dividendo % divisor
  print(f"O resto da divisão de {dividendo} por {divisor} é: {resto}")

resto_divisao()