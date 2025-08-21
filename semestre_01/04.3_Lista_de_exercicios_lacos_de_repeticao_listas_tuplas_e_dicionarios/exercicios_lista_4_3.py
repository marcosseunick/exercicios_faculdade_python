import os
import platform


def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Exercício 1
def exercicio1():
    limpar_tela()
    print("=== Exercício 1: Escreva um programa que imprima os números de 1 a 100 usando um laço for. ===")
    for i in range(1,101):
        print(i)

# Exercício 2
def exercicio2():
    limpar_tela()
    print("=== Exercício 2: Faça um programa que exiba os múltiplos de 5 entre 0 e 100 usando while. ===")
    numeros = 0
    while numeros <= 100:
        print(numeros)
        numeros += 5

# Exercício 3
def exercicio3():
    limpar_tela()
    print("=== Exercício 3: 10 números ao usuário e exiba a média aritmética. ===")
    lista = []
    for i in range(10):
        numeros = int(input("Digite um número: "))
        lista.append(numeros)
    media = sum(lista) / len(lista)
    print(media)



exercicios = {
    '1': {'titulo': '1 a 100 usando um laço for', 'funcao': exercicio1},
    '2': {'titulo': 'Múltiplos de 5 entre 0 e 100 usando while.', 'funcao': exercicio2},
    '3': {'titulo': 'Múltiplos de 5 entre 0 e 100 usando while.', 'funcao': exercicio3},
    # Adicione mais exercícios conforme necessário
}


def mostrar_menu():
    limpar_tela()
    print("=== BIBLIOTECA DE EXERCÍCIOS ===")
    for num, ex in exercicios.items():
        print(f"{num}. {ex['titulo']}")
    print("\n0. Sair")
    print("===============================")


def main():
    while True:
        mostrar_menu()
        opcao = input("\nDigite o número do exercício: ")
        
        if opcao == '0':
            limpar_tela()
            print("Programa encerrado. Até mais!")
            break
            
        if opcao in exercicios:
            while True:
               
                exercicios[opcao]['funcao']()
                
                
                repetir = input("\nDeseja executar novamente? (s/n): ").lower()
                if repetir != 's':
                    break
        else:
            input("\nOpção inválida! Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
