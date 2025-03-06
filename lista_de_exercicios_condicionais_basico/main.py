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

# 2 - Crie uma variável idade e atribua um valor numérico. Verifique se a pessoa é maior de 18 anos. Se for, exiba "Maior de idade", caso contrário, exiba "Menor de idade".

def validar_entrada(mensagem):
  while True:
    try:
      valor = int(input(mensagem))
      if valor >= 18 or valor < 18:
        return valor
    except ValueError:
      print("Entrada Inválida. Digite um número Válido: ")

idade = 18

idade_usuario = validar_entrada("Quantos anos você tem? ")
if idade_usuario >= idade:
  print("Você é maior de idade")
elif idade_usuario < idade:
  print("Você é menor de idade")

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

# 5 - Crie três variáveis lado1, lado2 e lado3 representando os lados de um triângulo. 
# Verifique se é um triângulo equilátero (todos os lados iguais),isósceles (dois lados iguais) ou escaleno (todos os lados diferentes).

def validar_entrada(mensagem):
  while True:
    try:
      valor = float(input(mensagem))
      if valor >= 1:
        return valor
      print("Número inválido, tente novamente")
    except ValueError:
      print("Entrada Inválida. Digite um número Válido.")

while True:
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
    break
  else:
    print("Triângulo Inválido! Digite os valores novamente")

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

# 7 - Crie uma variável mes e atribua um valor de 1 a 12 representando um mês. Exiba o nome do mês correspondente (por exemplo, se mes for 1, exiba "Janeiro").

def validar_entrada(mensagem):
  while True:
    try:
      valor = int(input(mensagem))
      if valor >= 1:
        return valor
      print("Número inválido, tente novamente")
    except ValueError:
      print("Entrada Inválida. Digite um número Válido.")

mes = validar_entrada("Digite um número de 1 a 12: ")
if mes == 1:
  print("Janeiro")
elif mes == 2:
  print("Fevereiro")
elif mes == 3:
  print("Março")
elif mes == 4:
  print("Abril")
elif mes == 5:
  print("Maio")
elif mes == 6:
  print("Junho")
elif mes == 7:
  print("Julho")
elif mes == 8:
  print("Agosto")
elif mes == 9:
  print("Setembro")
elif mes == 10:
  print("Outubro")
elif mes == 11:
  print("Novembro")
elif mes == 12:
  print("Dezembro")
else:
  print("Mês Inválido")

# 8 - Crie uma variável ano e atribua um valor numérico. Verifique se o ano é bissexto. Se for, exiba "Ano bissexto", caso contrário, exiba "Ano não bissexto".

def validar_entrada(mensagem):
  while True:
    try:
      valor = int(input(mensagem))
      if valor >= 1:
        return valor
      print("Número Inválido. O número tem que ser maior que 0")
    except ValueError:
      print("Entrada Inválida. Digite um número válido")

ano = validar_entrada("Digite algum ano: ")
bissexto = "É bissexto" if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else "Não é bissexto"
print(bissexto)

# 9 - Peça ao usuário para inserir um número. Se o número estiver entre 10 e 20 (inclusive), exiba "Número entre 10 e 20", caso contrário, exiba "Número fora do intervalo".

def validar_entrada(mensagem):
  while True:
    try:
      valor = float(input(mensagem))
      if valor >= 1:
        return valor
      print("Número Inválido. O número tem que ser maior que 0")
    except ValueError:
      print("Entrada Inválida. Digite um número válido")

numero = validar_entrada("Digite um Número: ")
verificacao = "Número entre 10 e 20" if numero > 10.0 and numero < 20.0 else "Número fora do intervalo"
print(verificacao)
