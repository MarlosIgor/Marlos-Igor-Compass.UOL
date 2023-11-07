# tabela verdade do AND
print(7 != 3 and 2 > 3)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# tabela verdade do OR
print(7 != 3 or 2 > 3)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# tabela verdade XOR
print((7 != 3) != (2 > 3))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# operador de negacao
print(not True)
print(not False)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# ex:
saldo = 1000
salario = 4000
despesas = 2967

meta = saldo > 0 and salario - despesas >= 0.2 * salario
print(meta)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# ou
saldo1 = 1000
salario1 = 4000
despesas1 = 2967

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

print(saldo_positivo and despesas_controladas)
