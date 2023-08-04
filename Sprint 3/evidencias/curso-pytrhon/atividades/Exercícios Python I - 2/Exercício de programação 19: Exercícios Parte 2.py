import random

random_list = random.sample(range(500), 50)

random_list.sort()

mediana = 0
if len(random_list) % 2 == 0:
    mediana = (random_list[int(len(random_list)/2)] + random_list[int(len(random_list)/2)-1])/2
else:
    mediana = random_list[int(len(random_list)/2)]

media = sum(random_list) / len(random_list)

valor_minimo = min(random_list)

valor_maximo = max(random_list)

print(f'Media: {media}', end=', ')
print(f'Mediana: {mediana}', end=', ')
print(f'Mínimo: {valor_minimo}', end=', ')
print(f'Máximo: {valor_maximo}')

