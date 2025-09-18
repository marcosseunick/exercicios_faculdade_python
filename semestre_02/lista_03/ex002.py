# Dado um valor de saque e um vetor com as cédulas disponíveis e suas quantidades (ex.: {100:2, 50:3, 20:5, 10:8}), 
# calcule uma combinação que usa a menor quantidade total de cédulas. Se for impossível, informe.
# Entrada (exemplo): saque=380, cédulas: {100:2, 50:1, 20:5, 10:10}
# Saída (exemplo): {100:2, 50:1, 20:1, 10:1}
# Obs.: se não houver solução, imprimir impossivel.


cedulas_disponiveis = {100: 2, 50: 1, 20: 5, 10: 10}
resultado_saque = {}

print("Bem-vindo ao Caixa Eletrônico!")
print(f"As cédulas disponíveis são: {cedulas_disponiveis}")


try:
    saque = int(input("Digite o valor que deseja sacar: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
    exit() 
valor_restante = saque



cedulas_ordenadas = sorted(cedulas_disponiveis.keys(), reverse=True)

for valor_cedula in cedulas_ordenadas:
    if valor_restante < valor_cedula:
        continue
    
    quantidade_necessaria = valor_restante // valor_cedula
    quantidade_disponivel = cedulas_disponiveis[valor_cedula]
    quantidade_a_usar = min(quantidade_necessaria, quantidade_disponivel)

    if quantidade_a_usar > 0:
        resultado_saque[valor_cedula] = quantidade_a_usar
        valor_restante -= quantidade_a_usar * valor_cedula


if valor_restante == 0:
    print("\nSaque realizado com sucesso!")
    print(f"Cédulas entregues: {resultado_saque}")
else:
    print(f"\nNão é possível sacar o valor de R${saque} com as cédulas disponíveis.")
    print("O valor restante que não pôde ser sacado foi de R$", valor_restante)