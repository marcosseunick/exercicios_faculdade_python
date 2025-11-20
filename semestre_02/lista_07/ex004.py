import matplotlib.pyplot as plt
import numpy as np


np.random.seed(42) 
notas = np.random.uniform(0, 10, 50)


plt.hist(notas, bins=10, color='purple', edgecolor='black', alpha=0.7)
plt.title("Distribuição de Notas da Turma")
plt.xlabel("Notas")
plt.ylabel("Quantidade de Alunos")
plt.show()