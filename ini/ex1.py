animais = ["Cachorro", "Gato", "Papagaio"]
animais.append("Rato")
animais.append("Jacaré")

animais2 = []

for i in range(3):
    animais2.append(animais[i+1])

print(animais2)