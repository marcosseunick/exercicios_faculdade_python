# def encontrar_primeiro_menor(lista: list):
#     if not lista:
#         print("A lista está vazia.")
#         return

#     menor_valor = min(lista)

#     posicao = lista.index(menor_valor)


#     print(f"O menor valor na lista é: {menor_valor}")
#     print(f"Ele está na posição (índice): {posicao}")

# print("--- Teste 1 ---")
# encontrar_primeiro_menor([1, 2, 3, 4, 5, 6])

# print("\n--- Teste 2 ---")
# encontrar_primeiro_menor([5, 2, 8, 1, 4]) 


def selection_sort(lista: list) -> list:
    for i in range(len(lista)):
        indice_do_menor = i

        for j in range(i + 1, len(lista)): 
            if lista[j] < lista[indice_do_menor]: 
                indice_do_menor = j

        lista[i], lista[indice_do_menor] = lista[indice_do_menor], lista[i]



exemplo = [5,4,7,0,8,1,2,9,3,6]
print(exemplo)
selection_sort(exemplo)
print(exemplo)