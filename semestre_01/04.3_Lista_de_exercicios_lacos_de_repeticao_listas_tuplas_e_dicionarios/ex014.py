#Conte quantos números digitados pelo usuário são positivos. O programa deve parar quando um número negativo for digitado.

contador_positivos = 0 

print("Digite números (um negativo para parar):")

while True:
    numero = float(input("Número: "))  
    if numero < 0:
        break
    contador_positivos += 1 
print(f"Quantidade de números positivos digitados: {contador_positivos}")