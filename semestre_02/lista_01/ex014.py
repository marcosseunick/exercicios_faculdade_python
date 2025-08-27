# Função comparar_numeros()
# Peça dois números e informe se o primeiro é maior que o segundo.

def comparar_numeros():

  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))

  resultado = num1 > num2
  print(f"O primeiro número é maior que o segundo? {resultado}")

comparar_numeros()