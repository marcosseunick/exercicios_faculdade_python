import pandas as pd


dados = {
    'Jogador': ['Marcos', 'Luisa', 'Pedro', 'Julia'],
    'Pontos': [1500, 3200, 1800, 2900]
}
df = pd.DataFrame(dados)

ranking = df.sort_values(by='Pontos', ascending=False)

print("--- Ranking ---")
print(ranking)


campeao = ranking.iloc[0]
print(f"\n🏆 Campeão: {campeao['Jogador']} com {campeao['Pontos']} pontos!")