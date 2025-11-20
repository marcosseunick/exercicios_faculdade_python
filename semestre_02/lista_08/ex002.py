import pandas as pd


dados = [
    {'nome': 'Arroz', 'quantidade': 50, 'preco': 20.50},
    {'nome': 'Feijão', 'quantidade': 30, 'preco': 8.90},
    {'nome': 'Macarrão', 'quantidade': 100, 'preco': 5.00}
]
df = pd.DataFrame(dados)

df['Total Item'] = df['quantidade'] * df['preco']


valor_total_estoque = df['Total Item'].sum()

print(f"Valor total do estoque: R$ {valor_total_estoque:.2f}")