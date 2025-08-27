# Função mostrar_tipos_dados()
# Leia um valor inteiro, um valor decimal e uma palavra, e depois mostre na tela cada valor e seu respectivo tipo.

def mostrar_tipos_dados():

  valor_inteiro = int(input("Digite um número inteiro: "))
  valor_decimal = float(input("Digite um número decimal (ex: 10.5): "))
  palavra = input("Digite uma palavra: ")

  print(f"O valor '{valor_inteiro}' é do tipo: {type(valor_inteiro)}")
  print(f"O valor '{valor_decimal}' é do tipo: {type(valor_decimal)}")
  print(f"O valor '{palavra}' é do tipo: {type(palavra)}")

mostrar_tipos_dados()