import random
import names

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]

with open('nomes_aleatorios.txt', 'w') as f:
    for nome in dados:
        f.write("%s\n" % nome)
