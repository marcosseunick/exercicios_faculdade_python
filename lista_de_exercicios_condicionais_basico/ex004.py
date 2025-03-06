# 4 - Peça ao usuário para inserir um número. Se o número for par, exiba "Número par". Se for ímpar, exiba "Número ímpar".

def validar_entrada(mensagem):
  while True:
    try:
      valor = float(input(mensagem))
      if valor >= 1:
        return valor
      print("Número inválido, tente novamente")
    except ValueError:
      print("Entrada Inválida. Digite um número Válido: ")

num = validar_entrada("Digite um Número: ")

if num % 2 == 0:
  print("Número Impar")
else:
  print("Número Par")
