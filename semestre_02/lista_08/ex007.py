import pandas as pd
import matplotlib.pyplot as plt


dados = {
    'Produto': ['Teclado', 'Mouse', 'Monitor', 'Teclado'],
    'Quantidade': [10, 20, 5, 5],
    'Preco': [100, 50, 800, 100]
}
df = pd.DataFrame(dados)


df['Faturamento'] = df['Quantidade'] * df['Preco']


vendas_totais = df.groupby('Produto')['Faturamento'].sum()

print(vendas_totais)


vendas_totais.plot(kind='bar', color='green', title='Faturamento por Produto')
plt.ylabel('Valor (R$)')
plt.show()