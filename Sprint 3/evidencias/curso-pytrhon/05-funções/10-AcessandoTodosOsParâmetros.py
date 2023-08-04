def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    todos_params('a', 'b', 'c')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    todos_params(1,2,3, [1, 2, 3], tamanho='M', fragil=False)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    todos_params(primeiro='Joao', segundo='Maria')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    todos_params('Maria', primeiro='Joao')