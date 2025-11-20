import pandas as pd


dados = [
    {'data': '2025-01-01', 'temperatura': 28, 'chuva': True},
    {'data': '2025-01-02', 'temperatura': 32, 'chuva': False},
    {'data': '2025-01-03', 'temperatura': 25, 'chuva': True},
    {'data': '2025-01-04', 'temperatura': 30, 'chuva': False}
]
df = pd.DataFrame(dados)

media_temp = df['temperatura'].mean()

dias_chuvosos = df['chuva'].sum() 

print(f"Temperatura Média: {media_temp:.1f}°C")
print(f"Dias com chuva: {dias_chuvosos}")