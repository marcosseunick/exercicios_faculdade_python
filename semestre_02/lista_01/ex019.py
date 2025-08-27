# Função dobrar_valor()
# Receba um número e troque o valor dessa variável para o dobro do valor digitado, depois exiba.

def dobrar_valor():

  numero = float(input("Digite um número: "))
  print(f"O valor original da variável é: {numero}")
  
  numero = numero * 2
  
  print(f"O novo valor (dobrado) da variável é: {numero}")

dobrar_valor()