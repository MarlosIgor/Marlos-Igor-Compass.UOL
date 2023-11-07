#!/usr/local/bin/python3
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print('''\
        E necessario informar o raio do circulo.
        Sintaxe: {} <raio>'''.format(sys.argv[0][53:]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Area do circulo', area)
