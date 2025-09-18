def calcular_ranking(matriz_placar):
   
    num_times = len(matriz_placar)
    
    estatisticas = [
        {
            'id': i,
            'nome': f"Time {i + 1}",
            'pontos': 0,
            'gols_pro': 0,
            'gols_contra': 0,
            'saldo': 0
        } for i in range(num_times)
    ]

    for i in range(num_times):
        for j in range(i + 1, num_times):
            gols_time_i = matriz_placar[i][j]
            gols_time_j = matriz_placar[j][i]

            estatisticas[i]['gols_pro'] += gols_time_i
            estatisticas[i]['gols_contra'] += gols_time_j
            estatisticas[j]['gols_pro'] += gols_time_j
            estatisticas[j]['gols_contra'] += gols_time_i

            if gols_time_i > gols_time_j:  
                estatisticas[i]['pontos'] += 3
            elif gols_time_j > gols_time_i: 
                estatisticas[j]['pontos'] += 3
            else: 
                estatisticas[i]['pontos'] += 1
                estatisticas[j]['pontos'] += 1

   
    for time in estatisticas:
        time['saldo'] = time['gols_pro'] - time['gols_contra']

    ranking_final = sorted(
        estatisticas,
        key=lambda time: (-time['pontos'], -time['saldo'], -time['gols_pro']),
        reverse=False
    )

    return ranking_final

def imprimir_ranking(ranking):

    print("--- Ranking Final do Campeonato ---")
    for i, time in enumerate(ranking):
        posicao = i + 1
        nome = time['nome']
        pontos = time['pontos']
        saldo = time['saldo']
        
       
        saldo_formatado = f"+{saldo}" if saldo >= 0 else str(saldo)
        
        print(f"{posicao}º {nome} ({pontos} pts, saldo {saldo_formatado})")


if __name__ == "__main__":
    
    placares = [
   
        [ 0,  2,  1,  3 ], 
        [ 1,  0,  1,  0 ], 
        [ 1,  1,  0,  4 ],
        [ 0,  2,  1,  0 ]  
    ]

    ranking = calcular_ranking(placares)
    imprimir_ranking(ranking)