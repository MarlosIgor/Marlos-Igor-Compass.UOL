def rm_duplicados(lista):
    return list(set(lista))


lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
nova_lista = rm_duplicados(lista)
print(nova_lista)
