# Função operacoes_basicas()
# Solicite dois números ao usuário e mostre:
# Soma
# Subtração
# Multiplicação
# Divisão

def operacoes_basicas():

  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))

  print(f"\nSoma: {num1} + {num2} = {num1 + num2}")
  print(f"Subtração: {num1} - {num2} = {num1 - num2}")
  print(f"Multiplicação: {num1} * {num2} = {num1 * num2}")
 
  if num2 != 0:
    print(f"Divisão: {num1} / {num2} = {num1 / num2}")
  else:
    print("Não é possível dividir por zero.")

operacoes_basicas()