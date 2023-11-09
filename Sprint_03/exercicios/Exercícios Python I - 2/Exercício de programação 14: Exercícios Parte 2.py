def parametros(*args, **kwargs):
    for arg in args:
        print(arg)
    for v in kwargs.values():
        print(f'{v}')


parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
