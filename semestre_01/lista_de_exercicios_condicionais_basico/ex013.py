# 13 - Desenvolva um algoritmo que receba do usuário os  valores a, b e c, de uma equação do segundo grau  (ax^2 + bx + c = 0) e determine as raízes.
import math

def validar_entrada(mensagem):
  while True:
    try:
      valor = float(input(mensagem))
      if valor > 0:
        return valor
      print("Valor Inválido. Digite um Número maior que 0")
    except ValueError:
      print("Entrada Inválida. Digite um número válido")

a = validar_entrada("Digite o coeficiente a: ")
b = validar_entrada("Digite o coeficiente b: ")
c = validar_entrada("Digite o coeficiente c: ")

delta = b ** 2 - 4 * a * c

if delta > 0:
  x1 = (-b + math.sqrt(delta)) / (2*a)
  x2 = (-b - math.sqrt(delta)) / (2*a)
  print(f"As raizes da equação são: x1 = {x1:.2f} e x2 = {x2:.2f}")
elif delta == 0:
  x = -b / (2*a)
  print(f"A equação tem uma raiz única real: x = {x:.2f}")
else:
  print("A equação não possuí raízes reais")