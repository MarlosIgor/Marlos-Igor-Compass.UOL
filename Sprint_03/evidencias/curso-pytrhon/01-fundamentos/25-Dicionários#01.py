pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': ['Ingles', 'Portugues']}
print(type(pessoa))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

print(len(pessoa))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][1])
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

print(pessoa.keys())
print(pessoa.values())
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

print(pessoa.get('nome'))