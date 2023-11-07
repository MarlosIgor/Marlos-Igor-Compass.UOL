for i in range(3):
    try:
        num = int(input('Digite um número: '))
    except EOFError:
        break

    if num % 2 == 0:
        print(f'Par: {num}')
    else:
        print(f'Ímpar: {num}')


