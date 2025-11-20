import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0, 10, 100)
x = np.sin(t) * t  
y = np.cos(t) * t  

plt.plot(x, y, marker='', linestyle='-', color='red', linewidth=2)
plt.scatter(x[0], y[0], color='green', label='Início', zorder=5) 
plt.scatter(x[-1], y[-1], color='black', label='Fim', zorder=5) 

plt.title("Rota da Corrida (GPS)")
plt.xlabel("Longitude (m)")
plt.ylabel("Latitude (m)")
plt.legend()
plt.grid(True)
plt.show()