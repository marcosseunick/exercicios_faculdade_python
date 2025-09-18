# Dada uma matriz R x C (0=livre, 1=ocupado), implemente: reservar assento, 
# liberar assento e verificar blocos contíguos de k lugares livres na mesma fila. Imprima um mapa final.
# Entrada (exemplo): R=3,C=5, matriz inicial com alguns 1s; operações: reservar(1,2), liberar(0,4), existe_bloco(k=3)
# Saída (exemplo): mapa final e existe_bloco=True.

def imprimir_mapa(mapa):

    if not mapa:
        print("Mapa de assentos está vazio.")
        return

    print("   " + " ".join([str(i) for i in range(len(mapa[0]))]))
    print("  " + "--" * len(mapa[0]))

    for i, fila in enumerate(mapa):
        print(f"{i}| " + " ".join(map(str, fila)))
    print()

def reservar_assento(mapa, fila, coluna):

    R = len(mapa)
    C = len(mapa[0])

    if not (0 <= fila < R and 0 <= coluna < C):
        print(f"Erro: Assento ({fila},{coluna}) está fora dos limites do mapa.")
        return

    if mapa[fila][coluna] == 0:
        mapa[fila][coluna] = 1
        print(f"Sucesso: Assento ({fila},{coluna}) reservado.")
    else:
        print(f"Aviso: Assento ({fila},{coluna}) já está ocupado.")

def liberar_assento(mapa, fila, coluna):

    R = len(mapa)
    C = len(mapa[0])

    if not (0 <= fila < R and 0 <= coluna < C):
        print(f"Erro: Assento ({fila},{coluna}) está fora dos limites do mapa.")
        return

    if mapa[fila][coluna] == 1:
        mapa[fila][coluna] = 0
        print(f"Sucesso: Assento ({fila},{coluna}) liberado.")
    else:
        print(f"Aviso: Assento ({fila},{coluna}) já estava livre.")

def existe_bloco_contiguo(mapa, k):

    if k <= 0:
        return False

    for fila in mapa:
        livres_seguidos = 0
        for assento in fila:
            if assento == 0:
                livres_seguidos += 1
                if livres_seguidos >= k:
                    return True 
                
                livres_seguidos = 0  
    
    return False 

if __name__ == "__main__":
    
    R = 3
    C = 5
    
    assentos = [
        [0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0]
    ]

    print("--- Mapa Inicial ---")
    imprimir_mapa(assentos)

    print("--- Executando Operações ---")
    
    reservar_assento(assentos, 0, 1) 
    liberar_assento(assentos, 0, 3)  
    print("-" * 28 + "\n")

 
    print("--- Mapa Final ---")
    imprimir_mapa(assentos)

   
    k = 3
    resultado_bloco = existe_bloco_contiguo(assentos, k)

    print(f"Verificando se existe um bloco de {k} lugares livres...")
    print(f"Saída existe_bloco: {resultado_bloco}")