import matplotlib.pyplot as plt
import numpy as np


temperaturas = np.array([30, 32, 31, 29, 28, 33, 34])
dias = np.arange(1, 8) 


media = np.mean(temperaturas)
minima = np.min(temperaturas)
maxima = np.max(temperaturas)

print(f"Média: {media:.2f}°C | Mínima: {minima}°C | Máxima: {maxima}°C")


plt.plot(dias, temperaturas, marker='o', linestyle='-', color='orange', label='Temp diária')
plt.axhline(media, color='blue', linestyle='--', label='Média') # Linha da média
plt.title("Variação de Temperatura")
plt.xlabel("Dias")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()