# Receba uma matriz 9x9 e verifique se é uma solução válida de Sudoku: todos os números de 1 a 9 em cada linha, coluna e subgrade 3x3. Informe o primeiro erro encontrado (linha/coluna/subgrade).
# Entrada (exemplo): matriz 9x9 preenchida
# Saída (exemplo): valida=True ou valida=False, erro=subgrade(1,1).

def validar_sudoku(matriz):
 
    valido, msg = validar_linhas(matriz)
    if not valido:
        return False, msg


    valido, msg = validar_colunas(matriz)
    if not valido:
        return False, msg

    valido, msg = validar_subgrades(matriz)
    if not valido:
        return False, msg

    return True, "Solução de Sudoku válida!"

def validar_grupo(grupo):

    return set(grupo) == set(range(1, 10))

def validar_linhas(matriz):

    for i, linha in enumerate(matriz):
        if not validar_grupo(linha):
            return False, f"linha({i})"
    return True, "OK"

def validar_colunas(matriz):
 
    for j in range(9):
        coluna = [matriz[i][j] for i in range(9)]
        if not validar_grupo(coluna):
            return False, f"coluna({j})"
    return True, "OK"

def validar_subgrades(matriz):

    for start_linha in range(0, 9, 3):
        for start_coluna in range(0, 9, 3):
            subgrade = []
            for i in range(3):
                for j in range(3):
                    subgrade.append(matriz[start_linha + i][start_coluna + j])
            
            if not validar_grupo(subgrade):
             
                idx_subgrade_linha = start_linha // 3
                idx_subgrade_coluna = start_coluna // 3
                return False, f"subgrade({idx_subgrade_linha},{idx_subgrade_coluna})"
    return True, "OK"



if __name__ == "__main__":
    
    
    sudoku_valido = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    sudoku_invalido = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 1], 
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    print("--- Verificando Matriz 1 (Válida) ---")
    valido, mensagem = validar_sudoku(sudoku_valido)
    if valido:
        print(f"Saída: valida={valido}")
    else:
        print(f"Saída: valida={valido}, erro={mensagem}")

    print("\n" + "-"*40 + "\n")

    print("--- Verificando Matriz 2 (Inválida) ---")
    valido, mensagem = validar_sudoku(sudoku_invalido)
    if valido:
        print(f"Saída: valida={valido}")
    else:
        print(f"Saída: valida={valido}, erro={mensagem}")

    sudoku_erro_subgrade = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 8], 
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    print("\n" + "-"*40 + "\n")
    print("--- Verificando Matriz 3 (Erro na Subgrade 1,1) ---")
    valido, mensagem = validar_sudoku(sudoku_erro_subgrade)
    if valido:
        print(f"Saída: valida={valido}")
    else:
        print(f"Saída: valida={valido}, erro={mensagem}")