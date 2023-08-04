a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

conj_a = set(a)
conj_b = set(b)

intersecao = list(conj_a.intersection(conj_b))
print(intersecao)
