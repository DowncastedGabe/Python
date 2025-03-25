ListaNomes = []

while True:
    nome = input("Digite um nome: ")
    ListaNomes.append(nome)

    continuar = input("Deseja continuar? Digite Sim ou Não ")
    if(continuar=="Não" or continuar=="NÃO"):
        break

print(ListaNomes)