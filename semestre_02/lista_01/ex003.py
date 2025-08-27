# Função mostrar_preco_produto()
# Receba o nome de um produto e seu preço e exiba:
# O produto [nome] custa R$ [preço].

def mostrar_preco_produto():

    nome = input("Digite o nome do produto: ")
    preco = int(input("Digite o preço do produto: "))
    
    print(f"O produto {nome} custa R${preco}.")

mostrar_preco_produto()