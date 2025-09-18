
COTIZACOES = {
    'USD': 1.0,    
    'BRL': 0.20,  
    'EUR': 1.08,  
    'JPY': 0.007,  
}

def converter(valor: float, de: str, para: str) -> float:

    de = de.upper()
    para = para.upper()

   
    if de not in COTIZACOES or para not in COTIZACOES:
        moedas_disponiveis = ", ".join(COTIZACOES.keys())
        raise ValueError(f"Moeda inválida. Moedas disponíveis: {moedas_disponiveis}")

    valor_em_usd = valor * COTIZACOES[de]
    
   
    valor_convertido = valor_em_usd / COTIZACOES[para]
    

    return round(valor_convertido, 2)