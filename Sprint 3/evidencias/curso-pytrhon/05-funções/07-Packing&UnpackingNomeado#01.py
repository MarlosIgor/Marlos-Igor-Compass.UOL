# **kwargs

# packing
def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='L. Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S. Vettel')


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


# unpacking
def resiltado_f2(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')


if __name__ == '__main__':
    podium = {'segundo': 'M. Verstappen',
              'primeiro': 'L. Hamilton',
              'terceiro': 'S. Vettel'}
    resiltado_f2(**podium)
