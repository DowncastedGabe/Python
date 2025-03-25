contatos = {
    "gulherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone":"3322-8181"}
}



resultado = "guilherme@gmail.com" in contatos #True
print(resultado)

resultado = "megui@gmail.com" in contatos #False
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"] # False

resultado = "telefone" in contatos["giovanna@gmail.com"] # True
print(resultado)