import pandas as pd


dados = [
    {'Usuario': 'U1', 'Filme': 'Matrix', 'Nota': 5},
    {'Usuario': 'U2', 'Filme': 'Matrix', 'Nota': 4},
    {'Usuario': 'U3', 'Filme': 'Titanic', 'Nota': 5},
    {'Usuario': 'U4', 'Filme': 'Titanic', 'Nota': 2},
    {'Usuario': 'U5', 'Filme': 'Shrek', 'Nota': 5}
]
df = pd.DataFrame(dados)


media_filmes = df.groupby('Filme')['Nota'].mean()

print("Média de Avaliação dos Filmes:")
print(media_filmes)