class Passaro:
    def voar(self):
        print(f'{self.__class__.__name__} Voando...')

    def emitir_som(self):
        pass


class Pato(Passaro):
    def emitir_som(self):
        print(f'{self.__class__.__name__} emitindo som... Quack Quack')


class Pardal(Passaro):
    def emitir_som(self):
        print(f'{self.__class__.__name__} emitindo som... Piu Piu')


pato = Pato()
pato.voar()
pato.emitir_som()

pardal = Pardal()
pardal.voar()
pardal.emitir_som()