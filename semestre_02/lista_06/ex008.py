def soma_digitos(n):
  
    if n < 10:
        return n
    
   
    else:
        return (n % 10) + soma_digitos(n // 10)
