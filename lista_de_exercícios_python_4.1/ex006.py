# Dada uma matriz 3x3 que represente o resultado de um jogo da velha, mostre uma mensagem com o estado atual do
# jogo. Usando as letras maiúsculas X e O, por exemplo

def mostrar_jogo_da_velha(tabuleiro):
    print("Estado atual do jogo da velha:")
    print("    1   2   3")
    for i in range(3):
        print(f"{i+1}  ", end="") 
        for j in range(3):
            print(f" {tabuleiro[i][j]} ", end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("   ---+---+---")


tabuleiro = [
    ['X', 'O', ' '],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

mostrar_jogo_da_velha(tabuleiro)