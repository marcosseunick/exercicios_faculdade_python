# 1 - Solicite ao usuário que insira um número. Se o número for positivo, exiba "Número positivo". Se for negativo, exiba "Número negativo". Se for zero, exiba "Zero".

def validar_entrada(mensagem):
  while True:
    try:
      valor = float(input(mensagem))
      if valor > 1 or valor < 1 or valor == 0:
        return valor
    except ValueError:
      print("Entrada Inválida. Digite um número Válido: ")


numero = validar_entrada("Digite um número: ")
if numero >= 1:
  print("Número Positivo")
elif numero < 0:
  print("Número Negativo")
elif numero == 0:
  print("Zero")
