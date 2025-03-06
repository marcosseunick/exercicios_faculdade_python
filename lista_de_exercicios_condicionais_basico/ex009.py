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