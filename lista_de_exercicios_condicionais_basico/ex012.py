#Crie um programa que simula o jogo Pedra, Papel e  Tesoura. Receba a escolha do usuário e compare  com uma escolha aleatória do computador.

from random import randint
from time import sleep

itens = ("pedra" , "papel" , "tesoura")
computador = randint(0, 2)

print('''Suas Ações:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input("Qual é a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)
print("-=" * 11)

print(f"Computador jogou: {itens[computador]}")
print(f"Jogador jogou: {itens[jogador]}")

if computador == 0:
  if jogador == 0:
    print("EMPATE")
  elif jogador == 1:
    print("JOGADOR VENCE!") 
  elif jogador == 2:
    print("COMPUTADOR VENCEU")
  else: 
    print("JOGADA INVÁLIDA")

if computador == 1:
  if jogador == 0:
    print("COMPUTADOR VENCEU")
  elif jogador == 1:
    print("EMPATE") 
  elif jogador == 2:
    print("JOGADOR VENCEU!")
  else: 
    print("JOGADA INVÁLIDA")

if computador == 2:
  if jogador == 0:
    print("JOGADOR VENCEU!")
  elif jogador == 1:
    print("COMPUTADOR VENCEU") 
  elif jogador == 2:
    print("EMPATE")
  else: 
    print("JOGADA INVÁLIDA")

