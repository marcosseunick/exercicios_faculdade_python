# Função verificar_idade_entre()
# Pergunte a idade de uma pessoa e verifique se ela tem entre 18 e 30 anos.

def verificar_idade_entre():
  
  idade = int(input("Digite sua idade: "))

  esta_no_intervalo = (idade >= 18) and (idade <= 30)

  print(f"Sua idade está entre 18 e 30 anos? {esta_no_intervalo}")

verificar_idade_entre()