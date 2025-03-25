contato = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contato.pop("guilherme@gmail.com") #dict_keys(['guilherme@gmail.com])
print(resultado)

resultado = contato.pop("gulherme@gmail.com", {})
print(resultado)