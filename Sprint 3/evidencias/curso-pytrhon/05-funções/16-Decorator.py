def log(funcion):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamanda da funcao: {funcion.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = funcion(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(soma(5, 7))

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    print(sub(5, y=7))


