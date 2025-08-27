# Função saudacao_usuario()
# Solicite ao usuário seu nome e sua idade e exiba a frase:
# Olá [nome], você tem [idade] anos.

def saudacao_usuario():

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    print(f"Olá {nome}, você tem {idade} anos.")

saudacao_usuario()