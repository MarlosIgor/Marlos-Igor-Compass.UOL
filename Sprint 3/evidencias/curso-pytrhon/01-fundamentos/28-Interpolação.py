from string import Template

nome, idade, peso = 'Ana', 30, 75.800
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# mais antiga
print('Nome: %s Idade: %d Peso: %.2f' % (nome, idade, peso))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# versao media
print('Nome: {} Idade: {} Peso: {}'.format(nome, idade, peso))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# versao mais nova aparti do python 3.6
print(f'Nome: {nome} Idade: {idade} Peso: {peso}')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

s = Template('Nome: $n Idade: $i')
print(s.substitute(n=nome, i=idade))