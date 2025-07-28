def verificar_anagrama(string1, string2):
    str1_limpa = sorted(string1.lower().replace(" ", ""))
    str2_limpa = sorted(string2.lower().replace(" ", ""))

    return str1_limpa == str2_limpa
print(verificar_anagrama("roma", "amor"))