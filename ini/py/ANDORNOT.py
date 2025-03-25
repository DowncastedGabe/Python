# Operador AND retorna verdadeiro se ambas expressões resultarem como verdadeira

a = 10
b = 10
c = 9
d = 8
if(a>=b)and(c>d):
    print("A é maior ou igual que b e c é maior que d")

# Operador OR Retorna verdadeiro se pelo menos uma das expressoes resultarem como verdadeira
a = 9
b = 9
c = 7
d = 4
if(a>=b)or(c>d):
    print("a é maior ou igual que b ou c é maior que d")
# Operador NOT Retorna verdadeiro se a expressão a direita for avaliada como falsa
a,b = 10,5
if not(a<b):
    print("A é menor que B")
