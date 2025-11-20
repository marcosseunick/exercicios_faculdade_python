def eh_palindromo(palavra):

    if len(palavra) <= 1:
        return True
    

    if palavra[0] == palavra[-1]:
 
        return eh_palindromo(palavra[1:-1])

    return False
