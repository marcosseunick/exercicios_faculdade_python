# 3 - Crie duas variáveis num1 e num2 e atribua valores diferentes. Verifique se num1 é igual a num2. Se forem iguais, exiba "Números iguais", caso contrário, exiba "Números diferentes".

def validar_entrada(mensagem):
  while True:
    try:
      valor = float(input(mensagem))
      if valor >= 1:
        return valor
      print("Número inválido, tente novamente")
    except ValueError:
      print("Entrada Inválida. Digite um número Válido: ")

num1 = validar_entrada("Digite um Número: ")
num2 = validar_entrada("Digite outro Número: ")
if num1 != num2:
  print("Números Diferentes")
elif num1 == num2:
  print("Números Iguais")