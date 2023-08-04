def my_map(list, f):
    nova_lista = []
    for i in list:
        nova_lista.append(f(i))
    return nova_lista


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = lambda x: x ** 2
potencia = my_map(lista, f)
print(potencia)