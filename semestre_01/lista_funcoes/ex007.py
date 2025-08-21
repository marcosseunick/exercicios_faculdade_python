def calcular_desconto(valor_produto, porcentagem):
    desconto = valor_produto * (porcentagem / 100)
    valor_final = valor_produto - desconto
    return valor_final
print(calcular_desconto(30, 5))