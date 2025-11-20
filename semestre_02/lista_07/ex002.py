import matplotlib.pyplot as plt
import numpy as np


dias = np.arange(1, 11)

alturas = np.array([2, 4, 5, 7, 8, 9, 11, 13, 14, 16])


coeficientes = np.polyfit(dias, alturas, 1) 
polinomio = np.poly1d(coeficientes) 
tendencia = polinomio(dias)


plt.scatter(dias, alturas, color='green', label='Medições Reais')
plt.plot(dias, tendencia, color='red', linestyle='--', label='Tendência Linear')
plt.title("Crescimento da Planta")
plt.xlabel("Dias")
plt.ylabel("Altura (cm)")
plt.legend()
plt.show()