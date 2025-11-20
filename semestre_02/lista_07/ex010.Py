import matplotlib.pyplot as plt
import numpy as np

horas = np.arange(0, 24)
sensor_interno = 22 + np.sin(horas/3) * 2  
sensor_externo = 20 + np.sin(horas/4) * 10 

plt.plot(horas, sensor_interno, label='Sensor Interno', color='blue')
plt.plot(horas, sensor_externo, label='Sensor Externo', color='orange')

plt.title("Monitoramento de Temperatura 24h")
plt.xlabel("Horas do dia")
plt.ylabel("Temperatura (°C)")
plt.legend() 
plt.grid(True)
plt.show()