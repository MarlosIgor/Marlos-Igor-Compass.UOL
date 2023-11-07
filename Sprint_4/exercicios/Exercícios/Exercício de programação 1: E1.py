with open('number.txt', 'r') as file:
    numbers = map(int, file.readlines())
    numeros_pares = list(filter(lambda x: x % 2 == 0, numbers))
    sorted_numeros_pares = sorted(numeros_pares, reverse=True)
    cinco_maiores = sorted_numeros_pares[:5]
    total = sum(cinco_maiores)

    print(cinco_maiores)
    print(total)
