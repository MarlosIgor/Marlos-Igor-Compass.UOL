class Potencia:
    # Calcula uma potencia especifica

    # construtor __init__, expoente e um paramertro
    def __init__(self, expoente):
        self.expoente = expoente

    # funcao __call--, base e um paramertro
    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'3² => {quadrado(3)}') # 3 elevado ao quadrado
        print(f'3² => {cubo(5)}') # 5 elevado ao cubo
        print(Potencia(4)(2)) # elevado a 4
