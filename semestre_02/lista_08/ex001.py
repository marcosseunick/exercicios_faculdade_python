import pandas as pd

dados = {
    'Aluno': ['Ana', 'Ana', 'Ana', 'Beto', 'Beto', 'Beto', 'Carla'],
    'Data': ['01/11', '02/11', '03/11', '01/11', '02/11', '03/11', '01/11'],
    'Presente': [True, False, True, True, True, False, False] 
}
df = pd.DataFrame(dados)

faltas = df[df['Presente'] == False]


total_faltas = faltas.groupby('Aluno')['Data'].count()

print("Total de Faltas por Aluno:")
print(total_faltas)