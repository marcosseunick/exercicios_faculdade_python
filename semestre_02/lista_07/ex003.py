import matplotlib.pyplot as plt
import numpy as np

dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex']
vendedor_A = [10, 15, 7, 12, 20]
vendedor_B = [12, 13, 9, 11, 18]

x = np.arange(len(dias))  
largura = 0.35 

plt.bar(x - largura/2, vendedor_A, width=largura, label='Vendedor A', color='blue')
plt.bar(x + largura/2, vendedor_B, width=largura, label='Vendedor B', color='green')

plt.xticks(x, dias) 
plt.title("Vendas Semanais")
plt.legend()
plt.show()