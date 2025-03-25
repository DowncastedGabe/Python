def elementos_comuns(listal, lista2):
    set1 = set(map(int, listal))
    set2 = set(map(int, lista2))
    return list(set1.intersection(set2))

# Leitura das listas
listal = input().split()
lista2 = input().split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in listal) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(listal, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")