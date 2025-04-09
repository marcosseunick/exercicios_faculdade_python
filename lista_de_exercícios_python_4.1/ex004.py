# 4. Dada uma matriz de 3x3 preenchida com números inteiros e imprima a soma dos elementos da diagonal principal.

matriz = [[0, 1, 2],
          [3, 5, 8],
          [9, 14, 30]]

soma_diagonal = 0
for i in range(3):
    soma_diagonal += matriz[i][i]
print("A soma da diagonal principal é", soma_diagonal)