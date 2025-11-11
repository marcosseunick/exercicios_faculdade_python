# Análise de Vendas com statistics
# Enunciado: Escreva funções para calcular média, mediana, moda e desvio-padrão 
# de um vetor de vendas mensais e outra função para detectar outliers via z-score (|z|>2). 
# Não use bibliotecas externas.
# Entrada (exemplo): vendas=[10,12,13,11,60,12,14,13]
# Saída (exemplo): media=18.13, mediana=12.5, outliers=[60].

def calcular_media(dados):
    
    if not dados:
        return 0
    return sum(dados) / len(dados)

def calcular_moda(dados):
    if not dados:
        return 0
    dados_ordenados = sorted(dados)
    n =len(dados_ordenados)
    ponto_medio = n//2

    if n % 2 == 1:
        return dados_ordenados[ponto_medio]
    else:
        return (dados_ordenados[ponto_medio - 1]) + dados_ordenados[ponto_medio] / 2
    
def calcular_moda(dados):
   
    if not dados:
        return []
    
    contagem = {}
    for item in dados:
        contagem[item] = contagem.get(item, 0) + 1
        
    
    max_frequencia = 0
    for freq in contagem.values():
        if freq > max_frequencia:
            max_frequencia = freq
            
    
    if max_frequencia == 1:
        return []
        
    
    modas = []
    for num, freq in contagem.items():
        if freq == max_frequencia:
            modas.append(num)
            
    return modas

def calcular_desvio_padrao(dados, media):
    
    if len(dados) < 2:
        return 0
        
    
    soma_diferencas_quadradas = 0
    for valor in dados:
        soma_diferencas_quadradas += (valor - media) ** 2
        
   
    variancia = soma_diferencas_quadradas / (len(dados) - 1)
    
    
    return variancia ** 0.5

def detectar_outliers_zscore(dados):
  
    if not dados or len(dados) < 2:
        return []

    media = calcular_media(dados)
    desvio_padrao = calcular_desvio_padrao(dados, media)
    

    if desvio_padrao == 0:
        return []

    outliers = []
    for valor in dados:
        z_score = (valor - media) / desvio_padrao
        if z_score > 2 or z_score < -2: 
            outliers.append(valor)
            
    return outliers


    