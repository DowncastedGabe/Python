nome = ""
continuar = True
while continuar:
    nome = nome + input("Digite um nome: ") + "\n"

    x = input("Deseja continuar? digite 'Sim' ou 'Não' ")
    if(x.upper() =="SIM"):
        continuar = True
    else:
        continuar = False

print(nome)