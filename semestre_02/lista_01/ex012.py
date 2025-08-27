# Função aplicar_desconto()
# Receba o valor de um produto e aplique 10% de desconto, mostrando o valor final.

def aplicar_desconto():

  valor_produto = float(input("Digite o valor do produto: R$ "))
  
  valor_final = valor_produto * 0.90 

  print(f"O valor com 10% de desconto é: R$ {valor_final:.2f}")

aplicar_desconto()