# Crie uma função chamada "encontrar_substring" que
# recebe uma string e uma substring como argumentos, e
# retorna True se a substring estiver presente na string, e
# False caso contrário.

def encontrar_substring(string, substring):
    if substring in string:
        return True
    else:
        return False