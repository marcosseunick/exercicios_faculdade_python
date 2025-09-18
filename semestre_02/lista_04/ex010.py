def validar_cpf(cpf: str) -> bool:

    cpf_numerico = ""
    for char in cpf:
        if char.isdigit():
            cpf_numerico += char

    if len(cpf_numerico) != 11:
        return False

    if len(set(cpf_numerico)) == 1:
        return False
  
    corpo_cpf = [int(d) for d in cpf_numerico[:9]]

    digitos_informados = [int(d) for d in cpf_numerico[9:]]

    soma = 0
   
    for i, digito in enumerate(corpo_cpf):
        soma += digito * (10 - i)
    
    resto = soma % 11
    digito_verificador_1 = 0 if resto < 2 else 11 - resto

    if digito_verificador_1 != digitos_informados[0]:
        return False
 
    corpo_cpf.append(digito_verificador_1)
    
    soma = 0
 
    for i, digito in enumerate(corpo_cpf):
        soma += digito * (11 - i)
        
    resto = soma % 11
    digito_verificador_2 = 0 if resto < 2 else 11 - resto

    if digito_verificador_2 != digitos_informados[1]:
        return False
        

    return True