#Crie um jogo de adivinhação: o computador escolhe um número de 1 a 100 e o usuário tenta adivinhar.
import random

numero_secreto = random.randint(1, 100)  # Corrigido: randint
tentativas = 0

while True:
    numero_usuario = int(input("Tente adivinhar o número que escolhi (1-100): "))
    tentativas += 1  # Conta cada tentativa

    if numero_usuario > numero_secreto:
        print("Muito Alto!")
    elif numero_usuario < numero_secreto:
        print("Muito Baixo!")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")  # Mensagem de vitória
        break