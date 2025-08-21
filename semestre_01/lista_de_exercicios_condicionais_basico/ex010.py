# 10 Crie um programa que recebe três números do usuário e determina qual é o maior número, utilizando apenas condicionais.

def validar_entrada(mensagem):
  while True:
    try:
      valor = float(input(mensagem))
      if valor >= 1:
        return valor
      print("Número Inválido. O número tem que ser maior que 0")
    except ValueError:
      print("Entrada Inválida. Digite um número válido")

num1 = validar_entrada("Digite um número: ")
num2 = validar_entrada("Digite mais um número: ")
num3 = validar_entrada("Digite o último número: ")
if num1 > num2 and num1 > num3:
  print(f"Número {num1} Maior")
elif num2 > num1 and num2 > num3:
  print(f"Número {num2} maior")
elif num3 > num2 and num3 > num1:
  print(f"Número {num3} maior")
else:
  print("Números iguais")