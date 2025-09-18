# Dado um vetor com o estoque inicial de produtos e uma sequência de operações no formato 
# "E codigo qtd" (entrada) ou "S codigo qtd" (saída), atualize o estoque.
# Impeça saídas maiores que o disponível e registre erros. Ao final, imprima o estoque e o total de operações inválidas.
# Entrada (exemplo): estoque inicial {A:10, B:3}, operações: E A 5, S B 2, S A 20
# Saída (exemplo): estoque final {A:15, B:1}, inválidas: 1 (por S A 20).

def controle_de_estoque(estoque: dict, operacoes: list[str]) -> None:
    invalidas = 0

    for operacao in operacoes:
        partes = operacao.split(" ")
        op = partes[0]
        chave = partes[1]
        valor= int(partes[2])

        if op == "E":
            estoque[chave] = valor
        else:
            if valor <= estoque[chave]:
                estoque[chave] -= valor
            else:
                invalidas += 1
    print(f"Estoque: {estoque}. Inválidas: {invalidas}")