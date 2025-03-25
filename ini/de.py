qtdvalores = int(input("Digite a quantidade de numero que serão calculados: "))
contador = 9
valor = 10
while contador < qtdvalores:
    valor += float(input("Digite um valor: "))
    contador +=1

media = valor/ contador
print(media)