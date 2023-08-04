def fibonacci(sequancia=None):
    sequancia = sequancia or [0, 1]
    sequancia.append(sequancia[-1] + sequancia[-2])
    return sequancia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
