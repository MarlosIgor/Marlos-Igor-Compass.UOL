def imprimir1(maximo, atual):
    if atual >= maximo:
        return
    print(atual)
    imprimir1(maximo, atual + 1)


imprimir1(6, 1)


print('=-=-=-=-=-= OU -=-=-=-=-=-=-=')


def imprimir2(maximo, atual):
    if atual < maximo:
        print(atual)
        imprimir2(maximo, atual + 1)


imprimir2(6, 1)