class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    # construtor com atributo que pertence a instancia
    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    grokn = Neanderthal('Grokn')
    print(f'Evolucao (a parte da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolucao (a parte da instancia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluido: {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluido? {Neanderthal.is_evoluido()}')
