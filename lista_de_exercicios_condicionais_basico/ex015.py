# Crie um programa dado solicite a largura e o  comprimento de uma sala (supondo que a sala seja quadrática), 
# solicite a largura e o tamanho do piso  e mostre quantos peças do preciso será necessário para revestir toda a sala

def validar_entrada(mensagem):
  while True:
    try:
      valor = float(input(mensagem))
      if valor > 0:
        return valor
      print("Valor Inválido. Digite um Número maior que 0")
    except ValueError:
      print("Entrada Inválida. Digite um número válido")

largura = validar_entrada("Digite a largura da sala em metros: ")
comprimento = validar_entrada("Digite o comprimento da sala em metros: ")
largura_do_piso = validar_entrada("Digite a largura do seu piso em metros: ")
tamanho_piso = validar_entrada("Digite o tamanho do seu piso em metros: ")

area_sala = largura * comprimento
area_piso = largura * tamanho_piso
quantidade_de_pecas = area_sala/area_piso

print(f"Você usará aproximadamente {quantidade_de_pecas} pisos")