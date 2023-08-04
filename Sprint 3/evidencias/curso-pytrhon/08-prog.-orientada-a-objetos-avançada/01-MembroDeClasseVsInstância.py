class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    # construtor com atributo que pertence a instancia
    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'


if __name__ == '__main__':
    jose = Humano('Jose')
    grokn = Humano('Grokn')
    grokn.das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')