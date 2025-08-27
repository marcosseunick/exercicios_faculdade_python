# Função potencia_e_raiz()
# Peça ao usuário um número e mostre:
# O quadrado desse número
# A raiz quadrada desse número

def potencia_e_raiz():

  numero = float(input("Digite um número: "))
  
  quadrado = numero ** 2
  raiz_quadrada = numero ** 0.5

  print(f"O quadrado de {numero} é: {quadrado}")
  print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")

potencia_e_raiz()