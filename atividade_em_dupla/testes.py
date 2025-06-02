import funcoes_com_listas
import funcoes_com_dicionarios

#1
assert funcoes_com_listas.criar_lista() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
assert funcoes_com_listas.criar_lista() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
assert funcoes_com_listas.criar_lista() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#2
assert funcoes_com_listas.adicionar_elemento(["A", "E", "I", "O"], "U") == ["A", "E", "I", "O", "U"]
assert funcoes_com_listas.adicionar_elemento([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5, 6]
assert funcoes_com_listas.adicionar_elemento(["Marcos", "Isabela", "Tirarão"], "Dez") == ["Marcos", "Isabela", "Tirarão", "Dez"]

#3
assert funcoes_com_listas.remover_elemento(["A", "E", "I", "O", "U"], "A") == ["E", "I", "O", "U"]
assert funcoes_com_listas.remover_elemento(['banana', 'laranja', 'maçã'], "maçã") == ['banana', 'laranja']
assert funcoes_com_listas.remover_elemento([1, 2, 3, 4, 5, 6, 7], 4) == [1, 2, 3, 5, 6, 7]

#4
assert funcoes_com_listas.contar_ocorrencias(["Hakuna", "Matata", "Timão", "Pumba", "Timão"], "Timão") == 2
assert funcoes_com_listas.contar_ocorrencias(["batata", "maionese", "carne", "arroz", "feijão"], "batata") == 1
assert funcoes_com_listas.contar_ocorrencias(["toddy", "sprite", "suco", "toddy", "toddy"], "toddy") == 3

#5
assert funcoes_com_listas.contem_elemento(["Arroz", "Frango", "Salada"], "Abacate") == False
assert funcoes_com_listas.contem_elemento(["Arroz", "Frango", "Salada"], "Arroz") == True
assert funcoes_com_listas.contem_elemento(["celular", "Computador", "Fone"], "Celular") == False

#6
assert funcoes_com_listas.inverter_lista(["Nós","Para","Dez", "Dar", "Vai", "Duda", "O"]) == ["O", "Duda", "Vai", "Dar", "Dez", "Para", "Nós"]
assert funcoes_com_listas.inverter_lista([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert funcoes_com_listas.inverter_lista(["Marcos", "Bob", "Charlie", "David"]) == ["David", "Charlie", "Bob", "Marcos"]

#7
assert funcoes_com_listas.ordenar_crescente([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]
assert funcoes_com_listas.ordenar_crescente([1, 2, 4, 3, 5]) == [1, 2, 3, 4, 5]
assert funcoes_com_listas.ordenar_crescente([20, 30, 10]) == [10, 20, 30]

#8
assert funcoes_com_listas.ordenar_decrescente([5, 2, 8, 1, 9]) == [9, 8, 5, 2, 1]
assert funcoes_com_listas.ordenar_decrescente([1, 2, 4, 3, 5]) == [5, 4, 3, 2, 1]
assert funcoes_com_listas.ordenar_decrescente([20, 30, 10]) == [30, 20, 10]

#9
assert funcoes_com_listas.somar_lista([1, 3, 4]) == 8
assert funcoes_com_listas.somar_lista([243, 464356, 2346234]) == 2810833
assert funcoes_com_listas.somar_lista([53, 21, 44]) == 118

#10
assert funcoes_com_listas.media_lista([6, 8, 10, 5]) == 7.25
assert funcoes_com_listas.media_lista([8, 30, 43, 7]) == 22
assert funcoes_com_listas.media_lista([50, 20, 24, 25]) == 29.75

#11
assert funcoes_com_listas.filtrar_pares([6, 8, 10, 5, 15, 432, 425]) == [6, 8, 10, 432]
assert funcoes_com_listas.filtrar_pares([8, 30, 43, 7]) == [8, 30]
assert funcoes_com_listas.filtrar_pares([50, 20, 24, 25]) == [50, 20, 24]

#12
assert funcoes_com_listas.quadrados([2, 4, 6]) == [4, 16, 36]
assert funcoes_com_listas.quadrados([8, 9, 10]) == [64, 81, 100]
assert funcoes_com_listas.quadrados([50, 20, 24, 25]) == [2500, 400, 576, 625]

#13
assert funcoes_com_listas.copiar_lista([2, 4, 6]) == [2, 4, 6]
assert funcoes_com_listas.copiar_lista([8, 9, 10]) == [8, 9, 10]
assert funcoes_com_listas.copiar_lista([50, 20, 24, 25]) == [50, 20, 24, 25]

#14
assert funcoes_com_listas.concatenar_listas(["Arroz"], ["Feijão"]) == ["Arroz", "Feijão"]
assert funcoes_com_listas.concatenar_listas(["Atividade"], ["Dez"]) == ["Atividade", "Dez"]
assert funcoes_com_listas.concatenar_listas(["Abacate"], ["Sushi"]) == ["Abacate", "Sushi"]

#15
assert funcoes_com_listas.limpar_lista([1, 2, 3, 4, 5]) == []
assert funcoes_com_listas.limpar_lista(['a', 'b']) == []
assert funcoes_com_listas.limpar_lista(['c', 'd']) == []