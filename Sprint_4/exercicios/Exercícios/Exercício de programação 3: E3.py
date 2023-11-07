from functools import reduce


def calcula_saldo(lancamentos) -> float:
    calcular_valor = lambda lancamento: lancamento[0] if lancamento[1] == 'C' else -lancamento[0]
    valores_calculados = map(calcular_valor, lancamentos)
    saldo_final = reduce(lambda acumulado, valor: acumulado + valor, valores_calculados, 0.0)

    return saldo_final


lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

saldo = calcula_saldo(lancamentos)
print(saldo)
