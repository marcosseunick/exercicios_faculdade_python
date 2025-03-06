# 6 - Peça ao usuário para inserir dois números. Se a soma dos números for maior que 100, exiba "Soma maior que 100", caso contrário, exiba "Soma menor ou igual a 100".

def validar_entrada(mensagem):
  while True:
    try:
      valor = int(input(mensagem))
      if valor >= 1:
        return valor
      print("Número inválido, tente novamente")
    except ValueError:
      print("Entrada Inválida. Digite um número Válido.")

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
soma = num1 + num2
resultado = "Maior que 100" if soma > 100 else "Menor que 100"
print(resultado)
