import matplotlib.pyplot as plt
import numpy as np


imagem = np.random.randint(0, 256, (10, 10))

imagem_invertida = 255 - imagem


fig, ax = plt.subplots(1, 2)

ax[0].imshow(imagem, cmap='gray', vmin=0, vmax=255)
ax[0].set_title("Original")

ax[1].imshow(imagem_invertida, cmap='gray', vmin=0, vmax=255)
ax[1].set_title("Invertida (Negativo)")

plt.show()