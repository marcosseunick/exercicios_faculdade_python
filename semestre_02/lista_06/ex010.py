def contar_troco(valor, moedas, indice_moeda=0):

    if valor == 0:
        return 1
    
   
    if valor < 0 or indice_moeda >= len(moedas):
        return 0
    
    
    usar_moeda = contar_troco(valor - moedas[indice_moeda], moedas, indice_moeda)
    

    pular_moeda = contar_troco(valor, moedas, indice_moeda + 1)
    
    return usar_moeda + pular_moeda


