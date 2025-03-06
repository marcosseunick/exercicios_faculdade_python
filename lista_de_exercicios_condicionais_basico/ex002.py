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