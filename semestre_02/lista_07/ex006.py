import matplotlib.pyplot as plt
import numpy as np

anos = np.arange(2015, 2025)
populacao = np.linspace(10000, 50000, 10)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))


ax1.plot(anos, populacao, marker='o')
ax1.set_title("Evolução Populacional")
ax1.grid(True)


ax2.pie(populacao, labels=anos, autopct='%1.1f%%', startangle=90)
ax2.set_title("Distribuição Relativa (Pizza)")

plt.show()