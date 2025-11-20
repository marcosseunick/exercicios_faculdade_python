import pandas as pd


dados = {
    'Linha': ['8055', '971R', '8055', '175T', '971R'],
    'Passageiros': [50, 30, 40, 20, 80]
}
df = pd.DataFrame(dados)


total_por_linha = df.groupby('Linha')['Passageiros'].sum()


linha_top = total_por_linha.idxmax()
qtd_top = total_por_linha.max()

print("Passageiros por linha:")
print(total_por_linha)
print(f"\n🚌 Linha mais movimentada: {linha_top} ({qtd_top} passageiros)")