
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, (pNome, sNome, idade) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f"{i} - {pNome} {sNome} está com {idade} anos")
