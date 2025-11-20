def desconto_progressivo(lista_precos, multiplicador=1):
    if not lista_precos:
        return 0
    else: 
        preco_atual = lista_precos[0]
        fator_pagamento = 1 - (0.10 * multiplicador)
        valor_com_desconto = preco_atual * fator_pagamento
        return valor_com_desconto + desconto_progressivo(lista_precos[1:], multiplicador + 1)
    