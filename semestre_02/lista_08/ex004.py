import pandas as pd


dados = {
    'Aluno': ['João', 'Maria', 'José', 'Ana'],
    'Prova1': [5.0, 7.0, 4.0, 9.0],
    'Prova2': [6.0, 8.0, 5.0, 9.5]
}
df = pd.DataFrame(dados)


df['Media'] = (df['Prova1'] + df['Prova2']) / 2


aprovados = df[df['Media'] >= 6.0]

print("Lista de Aprovados:")
print(aprovados[['Aluno', 'Media']])