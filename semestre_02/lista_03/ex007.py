# Dado um vetor de temperaturas diárias, calcule média, dias acima da média e a maior sequência consecutiva acima de um limiar L.
# Entrada (exemplo): temps: 28, 31, 33, 29, 30, 34, L=30
# Saída (exemplo): media=30.83, acima_media=3, maior_sequencia_acima_L=2.

def analisar_temperaturas(temps, limiar_L):
    
    if not temps:
        return {
            'media': 0,
            'acima_media': 0,
            'maior_sequencia_acima_L': 0
        }

   
    media = sum(temps) / len(temps)

    
    dias_acima_media = sum(1 for t in temps if t > media)

    maior_sequencia = 0
    sequencia_atual = 0
    for t in temps:
        if t > limiar_L:
          
            sequencia_atual += 1
        else:
          
            maior_sequencia = max(maior_sequencia, sequencia_atual)
            
            sequencia_atual = 0
    
    
    maior_sequencia = max(maior_sequencia, sequencia_atual)
  
    resultados = {
        'media': media,
        'acima_media': dias_acima_media,
        'maior_sequencia_acima_L': maior_sequencia
    }
    
    return resultados

if __name__ == "__main__":
    
    temperaturas_diarias = [28, 31, 33, 29, 30, 34, 32, 31, 28, 35, 36, 37]
    limiar = 30

    analise = analisar_temperaturas(temperaturas_diarias, limiar)

    print("--- Análise Climática Diária ---")
    print(f"Temperaturas: {temperaturas_diarias}")
    print(f"Limiar (L): {limiar}°C")
    print("-" * 32)
    
    print(f"Saída:")
    print(f"  - Média: {analise['media']:.2f}°C")
    print(f"  - Dias acima da média: {analise['acima_media']}")
    print(f"  - Maior sequência acima de {limiar}°C: {analise['maior_sequencia_acima_L']} dias")