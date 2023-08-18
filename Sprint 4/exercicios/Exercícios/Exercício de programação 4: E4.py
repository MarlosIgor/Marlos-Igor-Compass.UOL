def calcular_valor_maximo(operadores, operandos) -> float:
    resultados = list(map(lambda op, opnd: eval(f"{opnd[0]}{op}{opnd[1]}"), operadores, operandos))
    maior_valor = max(resultados)

    return maior_valor


operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

resultado_zip = calcular_valor_maximo(operadores, operandos)
print(resultado_zip)
