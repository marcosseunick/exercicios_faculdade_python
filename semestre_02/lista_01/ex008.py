# Função converter_string_para_inteiro()
# Receba do usuário um número em formato de texto (string) e converta-o para inteiro antes de realizar uma soma.

def converter_string_para_inteiro():

  numero_texto = input("Digite um número: ")
  print(f"O tipo original é: {type(numero_texto)}")

  numero_inteiro = int(numero_texto)
  print(f"O tipo após a conversão é: {type(numero_inteiro)}")

  resultado = numero_inteiro + 10
  print(f"O número {numero_inteiro} somado com 10 é: {resultado}")


converter_string_para_inteiro()