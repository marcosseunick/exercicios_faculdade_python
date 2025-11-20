import matplotlib.pyplot as plt
import numpy as np

dias = np.arange(1, 31)

precos = np.random.normal(100, 10, 30) 


indice_max = np.argmax(precos)
dia_max = dias[indice_max]
valor_max = precos[indice_max]

plt.plot(dias, precos, label='Preço Coin', color='gray')

plt.scatter(dia_max, valor_max, color='red', s=100, label=f'Máx: {valor_max:.2f}')

plt.title("Variação Criptomoeda (30 dias)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()