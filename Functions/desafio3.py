def contar_caracteres(string):
    #TODO: Initialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}
    
    #TODO: Tiere através de cada caractere na string string.
    for caractere in string:
        #TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1

    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)