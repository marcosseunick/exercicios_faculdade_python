import pandas as pd


dados = {
    'Nome': ['Ana', 'Bia', 'Carlos', 'Davi', 'Eva'],
    'Idade': [20, 25, 30, 22, 40],
    'Cidade': ['SP', 'RJ', 'SP', 'RJ', 'MG']
}
df = pd.DataFrame(dados)


media_idade = df.groupby('Cidade')['Idade'].mean()

print("Média de idade por cidade:")
print(media_idade)