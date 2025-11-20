import pandas as pd


dados = {
    'Data': ['01/10', '02/10', '03/10', '04/10'],
    'Categoria': ['Alimentação', 'Transporte', 'Alimentação', 'Lazer'],
    'Valor': [50.00, 20.00, 100.00, 150.00]
}
df = pd.DataFrame(dados)


gastos_categoria = df.groupby('Categoria')['Valor'].sum()


categoria_mais_cara = gastos_categoria.idxmax() 
valor_mais_caro = gastos_categoria.max()     

print(gastos_categoria)
print(f"\nCategoria mais custosa: {categoria_mais_cara} (R$ {valor_mais_caro})")