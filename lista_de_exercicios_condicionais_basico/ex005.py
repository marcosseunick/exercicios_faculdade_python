# 5 - Crie três variáveis lado1, lado2 e lado3 representando os lados de um triângulo. 
#Verifique se é um triângulo equilátero (todos os lados iguais),isósceles (dois lados iguais) ou escaleno (todos os lados diferentes).

def validar_entrada(mensagem):
  while True:
    try:
      valor = float(input(mensagem))
      if valor >= 1:
        return valor
      print("Número inválido, tente novamente")
    except ValueError:
      print("Entrada Inválida. Digite um número Válido.")


lado1 = validar_entrada("Digite o valor do lado 1: ")
lado2 = validar_entrada("Digite o valor do lado 2: ")
lado3 = validar_entrada("Digite o valor do lado 3: ")
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
  if lado1 == lado2 == lado3:
    print("Esse triângulo é Equilátero")
  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Esse triângulo é Isóceles")
  else:
    print("Esse triângulo é escaleno")
else:
  print("Triângulo Inválido! Digite os valores novamente")
