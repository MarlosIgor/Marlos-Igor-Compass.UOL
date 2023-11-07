def divide(lista):
  tl = len(lista)
  tp = tl // 3

  l1 = lista[:tp]
  l2 = lista[tp:2 * tp]
  l3 = lista[2 * tp:]

  return l1, l2, l3


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

l1, l2, l3 = divide(lista)

print(l1, end=' ')
print(l2, end=' ')
print(l3)