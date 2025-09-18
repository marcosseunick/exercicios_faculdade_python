# Enunciado: Leia as notas (0 a 10) de N alunos em uma lista. 
# Calcule média da turma, maior e menor nota, desvio-padrão (pode usar fórmula própria) 
# e quantos alunos ficaram acima da média. Mostre também a distribuição em faixas: [0–2), [2–4), [4–6), [6–8), [8–10].
# Entrada (exemplo): N=6 e notas: 7.5 9.0 4.0 6.5 8.0 5.0
# Saída (exemplo):
# media=6.67, maior=9.0, menor=4.0, acima_media=3
# faixas: [0-2)=0, [2-4)=0, [4-6)=2, [6-8)=2, [8-10]=2
import math

def ler_notas():
    numero_alunos = int(input("Digite o número de alunos: "))

    global notas

    notas = []
    print("Agora digite a nota de cada aluno: ")
    for i in range(numero_alunos):
        nota_aluno = float(input(f"Nota aluno {i+1}: "))
        notas.append(nota_aluno)
    print("Notas lidas com sucesso!")
    return notas 

def calcular_estatisticas(notas_recebidas):
    if not notas_recebidas:
        return 0, 0, 0, 0
    
    maior_nota = max(notas_recebidas)
    menor_nota = min(notas_recebidas)
    media_nota = sum(notas_recebidas) / len(notas_recebidas)
    
    alunos_acima_media = 0
    for nota in notas_recebidas:
        if nota > media_nota:
            alunos_acima_media += 1
            
    desvio_turma = []            
    for nota in notas:
        desvio_individual = nota - media_nota
        desvio_turma.append(desvio_individual**2)
        somar_desvio = sum(desvio_turma)
        desvio_geral = somar_desvio / len(notas)
        desvio_final = math.sqrt(desvio_geral)

    return maior_nota, menor_nota, media_nota, alunos_acima_media, desvio_final


def computar_faixas(notas):
    faixa_0_2 = 0
    faixa_2_4 = 0
    faixa_4_6 = 0
    faixa_6_8 = 0
    faixa_8_10 = 0

    for nota in notas:
        if nota >= 0 and nota < 2:
            faixa_0_2 += 1
        elif nota >= 2 and nota < 4:
            faixa_2_4 += 1
        elif nota >= 4 and nota < 6:
            faixa_4_6 += 1
        elif nota >= 6 and nota < 8:
            faixa_6_8 += 1
        elif nota >= 8 and nota <= 10: 
            faixa_8_10 += 1

    return faixa_0_2, faixa_2_4, faixa_4_6, faixa_6_8, faixa_8_10

lista_de_notas = ler_notas()

maior, menor, media, acima, desvio_final = calcular_estatisticas(lista_de_notas)
f1, f2, f3, f4, f5 = computar_faixas(lista_de_notas)

print("\n--- Resultados da Turma ---")
print(" ")
print(f"DESVIO = {desvio_final:.2f}")
print(f"MÉDIA= {media:.2f}")
print(f"MAIOR= {maior}")
print(f"MENOR= {menor}") 
print(f"ACIMA DA MÉDIA= {acima}")
print(" ")
print(f"faixas: [0-2)= {f1}, [2-4)= {f2}, [4-6)= {f3}, [6-8)= {f4} [8-10]= {f5}")
