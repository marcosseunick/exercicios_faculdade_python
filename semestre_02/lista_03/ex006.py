# Gere M cartelas (5x5) com números válidos (faixas por coluna) ou leia-as prontas. 
# Receba a sequência de números sorteados e identifique a primeira cartela vencedora (linha/coluna/diagonal completa).
# Entrada (exemplo): 2 cartelas 5x5 e sorteio: 7, 13, 22, ...
# Saída (exemplo): vencedora=cartela_2, criterio=diagonal_principal, chamadas=18.

import random


COLUNAS_BINGO = {
    0: ("B", range(1, 16)),
    1: ("I", range(16, 31)),
    2: ("N", range(31, 46)),
    3: ("G", range(46, 61)),
    4: ("O", range(61, 76))
}

def gerar_cartela():
   
    cartela = [[0 for _ in range(5)] for _ in range(5)]
    for col_idx, (_, num_range) in COLUNAS_BINGO.items():
  
        numeros_coluna = random.sample(list(num_range), 5)
        for linha_idx in range(5):
            cartela[linha_idx][col_idx] = numeros_coluna[linha_idx]
            
   
    cartela[2][2] = 0
    return cartela

def imprimir_cartela(cartela, id_cartela=None):
   
    if id_cartela:
        print(f"--- CARTELA {id_cartela} ---")
    
    print("  B   I   N   G   O")
    print("-" * 23)
    for linha in cartela:

        print(" ".join([f"{'XX':>2}" if num == 0 else f"{num:>2}" for num in linha]))
    print()

def marcar_numero_na_cartela(cartela, numero):
 
    for i in range(5):
        for j in range(5):
            if cartela[i][j] == numero:
                cartela[i][j] = 0
                return

def verificar_vitoria(cartela):
    
    for i in range(5):
        if sum(cartela[i]) == 0:
            return f"Linha {i + 1}"
            
   
    for j in range(5):
        if sum(cartela[i][j] for i in range(5)) == 0:
            return f"Coluna {COLUNAS_BINGO[j][0]}"
            
    
    if sum(cartela[i][i] for i in range(5)) == 0:
        return "Diagonal Principal"
        
   
    if sum(cartela[i][4 - i] for i in range(5)) == 0:
        return "Diagonal Secundária"
        
    return None


if __name__ == "__main__":
    M = 10 
    
    print(f"Gerando {M} cartelas de Bingo...")
    cartelas = [gerar_cartela() for _ in range(M)]

   
    for i in range(min(M, 3)):
        imprimir_cartela(cartelas[i], i + 1)

    
    numeros_sorteio = list(range(1, 76))
    random.shuffle(numeros_sorteio)

    print("\n--- COMEÇANDO O SORTEIO! ---\n")

    vencedora_encontrada = False
    info_vitoria = {}

    for i, numero_sorteado in enumerate(numeros_sorteio):
        chamadas = i + 1
        letra_coluna = next(c[0] for _, c in COLUNAS_BINGO.items() if numero_sorteado in c[1])
        print(f"Chamada {chamadas}: {letra_coluna}-{numero_sorteado}")

        for j, cartela in enumerate(cartelas):
            marcar_numero_na_cartela(cartela, numero_sorteado)
            
            
            criterio_vitoria = verificar_vitoria(cartela)
            if criterio_vitoria:
                vencedora_encontrada = True
                info_vitoria = {
                    'id': j + 1,
                    'criterio': criterio_vitoria,
                    'chamadas': chamadas,
                    'cartela_final': cartela
                }
                break 
        
        if vencedora_encontrada:
            break 

   
    if vencedora_encontrada:
        print("\n" + "="*15 + " BINGO! " + "="*15)
        print(f"Vencedora: Cartela {info_vitoria['id']}")
        print(f"Critério: {info_vitoria['criterio']}")
        print(f"Total de chamadas: {info_vitoria['chamadas']}")
        print("\nCartela Vencedora Final:")
        imprimir_cartela(info_vitoria['cartela_final'])
    else:
        
        print("\nO jogo terminou sem vencedores.")