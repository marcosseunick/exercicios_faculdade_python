# Crie um programa dado solicite a largura e o  comprimento de uma sala (supondo que a sala seja quadrática), 
# solicite a largura e o tamanho do piso  e mostre quantos peças do preciso será necessário para revestir toda a sala

largura = float(input("Digite a largura da sala: "))
comprimento = float(input("Digite o comprimento da sala: "))
largura_do_piso = float(input("Digite a largura do seu piso: "))
tamanho_piso = float(input("Digite o tamanho do seu piso: "))

area_sala = largura * comprimento
area_piso = largura * tamanho_piso
quantidade_de_pecas = area_sala/area_piso

print(f"Você usará aproximadamente {quantidade_de_pecas} pisos")