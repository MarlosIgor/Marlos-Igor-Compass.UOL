def soma(valor):
    numeros = valor.split(',')

    n = 0
    for i in numeros:
        n += int(i)
    return n


numeros = "1,3,4,6,10,76"
soma_numeros = soma(numeros)
print(soma_numeros)
