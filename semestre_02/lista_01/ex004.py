# Função converter_metros_para_centimetros()
# Solicite ao usuário um valor em metros e exiba esse valor convertido para centímetros.

def converter_metros_para_centimetros():
    metro = float(input("Digite um valor em metros: "))
    centimetros = metro * 100
    print(f"O valor em centímetros é de {centimetros}cm")

converter_metros_para_centimetros()