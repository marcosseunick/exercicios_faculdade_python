# Implemente um programa que solicita ao usuário o  ano de nascimento e classifica a faixa etária em  "Criança", "Adolescente", "Adulto Jovem" ou  "Adulto".

def validar_entrada(mensagem):
  while True:
    try:
      valor = int(input(mensagem))
      return valor
    except ValueError:
      print("Entrada Inválida. Digite um número válido")

idade = validar_entrada("Quantos anos você tem? ")
if idade < 12:
  print("Você é uma criança")
elif idade < 18:
  print("Você é um adolescente")
elif idade < 25:
  print("Você é um adulto jovem")
else:
  print("Você é um adulto")