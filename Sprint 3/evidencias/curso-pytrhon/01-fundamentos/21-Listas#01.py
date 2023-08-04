# criando uma lista vazia
lista = []
print(type(lista))
print(len(lista))

# adicionando 2 elementos
lista.append(1)
lista.append(2)
print(len(lista))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# criando uma nova lista
nova_lista = [1, 5, 'Ana', 'Bia']
print(nova_lista)

# removendo um item de uma lista
nova_lista.remove(5)
print(nova_lista)

# revertendo a lista
nova_lista.reverse()
print(nova_lista)

# adicionando uma nova lista dentro da lista
nova_lista.append([2, 3, 'Marlos'])
print(nova_lista)