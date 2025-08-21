def tem_caracteres_duplos(string): 
    string_lower = string.lower()
    caracteres_unicos = set() 
    for char in string_lower:
        if char in caracteres_unicos:
            return True   
        caracteres_unicos.add(char)
    return False

print(f"\"abca\" mostra {tem_caracteres_duplos('abca')}")
print(f"\"aabc\" mostra {tem_caracteres_duplos('aabc')}")
print(f"\"a 11 c d\" mostra {tem_caracteres_duplos('a 11 c d')}")
print(f"\"AabBcC\" mostra {tem_caracteres_duplos('AabBcC')}")
print(f"\"a b c\" mostra {tem_caracteres_duplos('a b c')}") # Note que aqui o espaço é o caractere duplicado
print(f"\"a b c d e f g h i h k\" mostra {tem_caracteres_duplos('a b c d e f g h i h k')}")
print(f"\"2020\" mostra {tem_caracteres_duplos('2020')}")