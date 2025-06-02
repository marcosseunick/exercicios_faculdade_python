#1
def criar_lista():
    lista = []
    for i in range(1, 21):
        lista.append(i)
    return lista

#2
def adicionar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

#3
def remover_elemento(lista, elemento):
    lista.remove(elemento)
    return lista

#4
def contar_ocorrencias(lista, elemento):
    return lista.count(elemento)

#5
def contem_elemento(lista, elemento):
    if elemento in lista:
        return True
    else:
        return False
    
#6
def inverter_lista(lista):
    lista.reverse()
    return lista

#7 
def ordenar_crescente(lista):
    lista.sort()
    return lista

#8
def ordenar_decrescente(lista):
    lista.sort(reverse=True)
    return lista

#9
def somar_lista(lista):
    return sum(lista)
    

#10 
def media_lista(lista): 
    return sum(lista) / len(lista)

#11
def filtrar_pares(lista):
    pares = [] 
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero) 
    return pares
#12
def quadrados(lista):
    quadrados_elementos = []  
    for numero in lista:
        quadrados_elementos.append(numero**2) 
    return quadrados_elementos

#13
def copiar_lista(lista):
    return lista.copy()
   
#14
def concatenar_listas(lista1, lista2):
    return lista1 + lista2

#15
def limpar_lista(lista):
    lista.clear()
    return lista
