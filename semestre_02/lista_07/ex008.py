import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-2, 4, 100)


y = x**2 - 2*x + 1

plt.plot(x, y, color='darkblue', linewidth=2)
plt.axhline(0, color='black', linewidth=0.8) 
plt.axvline(0, color='black', linewidth=0.8) 
plt.title(r"Projeção: $y = x^2 - 2x + 1$") 
plt.grid(True)
plt.show()