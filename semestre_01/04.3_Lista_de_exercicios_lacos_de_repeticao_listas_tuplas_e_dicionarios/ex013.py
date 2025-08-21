#Simule uma contagem regressiva de 10 a 0.

from time import sleep
for numero in range(10, -1, -1):
    print(numero)
    sleep(1)
print("ACABOU")