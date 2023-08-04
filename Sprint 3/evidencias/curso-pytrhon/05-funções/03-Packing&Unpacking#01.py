# funcao com 2 parametros
def soma_2(a, b):
    return a + b


# funcao com 3 parametros
def soma_3(a, b, c):
    return a + b + c


# funcao com varios parametros
def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    # packing
    print(soma_2(2, 3))
    print(soma_3(2, 4, 6))
    print(soma_n(2, 4, 7, 10))

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    # unpacking
    tupla_nums = (1, 2, 3)
    print(soma_3(*tupla_nums))
    lista_nums = [1, 2, 3]
    print(soma_3(*lista_nums))