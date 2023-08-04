a = {1, 2, 3}
print(type(a))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# faz a uniao, nao pode ter numeros repetidos
c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# ver os numeros repetidos
print(c1.intersection(c2))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# adicionandp o conjunto de c1 em c1
c1.update(c2)
print(c1)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

print(c1 <= c2)
print(c1 >= c2)
