# Dada uma matriz 3x3 que represente o resultado de um jogo da velha, mostre uma mensagem com o estado atual do
# jogo. Usando as letras maiúsculas X e O, por exemplo

def verificar_vencedor(tabuleiro, jogador):
    
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):
            return True
    
    for j in range(3):
        if all(tabuleiro[i][j] == jogador for i in range(3)):
            return True
    
    if all(tabuleiro[i][i] == jogador for i in range(3)) or \
       all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def mostrar_jogo_da_velha(tabuleiro):
    print("Estado atual do jogo da velha:")
    print("    1   2   3")
    for i in range(3):
        print(f"{i+1}   ", end="") 
        for j in range(3):
            print(f" {tabuleiro[i][j]} ", end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("   ---+---+---")

def analisar_estado_jogo(tabuleiro):
    if verificar_vencedor(tabuleiro, 'X'):
        print("\nO jogador X venceu!")
    elif verificar_vencedor(tabuleiro, 'O'):
        print("\nO jogador O venceu!")
    else:
        
        jogo_em_andamento = False
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == ' ':
                    jogo_em_andamento = True
                    break
            if jogo_em_andamento:
                break
        
        if jogo_em_andamento:
            print("\nO jogo está em andamento.")
        else:
            print("\nO jogo terminou em empate!")

tabuleiro = [
    ['X', 'O', ' '],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

mostrar_jogo_da_velha(tabuleiro)
analisar_estado_jogo(tabuleiro)
