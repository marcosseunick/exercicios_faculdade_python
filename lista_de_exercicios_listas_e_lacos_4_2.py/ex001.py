def encontrar_numero_impar_ocorrencias(arr):
    resultado = 0
    for numero in arr:
        resultado ^= numero
    return resultado


print(encontrar_numero_impar_ocorrencias([7]))  
print(encontrar_numero_impar_ocorrencias([0]))  
print(encontrar_numero_impar_ocorrencias([1, 1, 2]))  
print(encontrar_numero_impar_ocorrencias([0, 1, 0, 1, 0]))  
print(encontrar_numero_impar_ocorrencias([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))  