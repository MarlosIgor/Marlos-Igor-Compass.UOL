from datetime import datetime

idade = None

try:
    nome = input('Nome: ')
    idade = int(input("Idade: "))
except EOFError:
    pass

if idade is not None:
    ano_atual = datetime.now().year
    centenario = ano_atual + (100 - idade)
    print(centenario)
