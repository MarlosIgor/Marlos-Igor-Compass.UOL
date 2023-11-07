from decimal import Decimal, getcontext

print(1 / 7)

print(Decimal(1) / Decimal(7))

# 4 casas decimal
getcontext().prec = 4
print(Decimal(1) / Decimal(7))

# pega o maior valor
print(Decimal.max(Decimal(1), Decimal(7)))

