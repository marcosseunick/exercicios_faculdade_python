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