# Função verificar_tres_iguais()
# Receba três números e verifique se todos são iguais (usando operador lógico and).

def verificar_tres_iguais():

  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))
  num3 = float(input("Digite o terceiro número: "))

  sao_iguais = (num1 == num2) and (num2 == num3)
  print(f"Todos os números são iguais? {sao_iguais}")

verificar_tres_iguais()