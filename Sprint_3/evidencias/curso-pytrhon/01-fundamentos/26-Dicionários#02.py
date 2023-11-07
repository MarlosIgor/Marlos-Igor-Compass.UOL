pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}

# altera o valor da chave
pessoa['idade'] = 44
print(pessoa)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# adiciona um item na lista
pessoa['cursos'].append('Java')
print(pessoa)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# ler o atributo e dps apaga
pessoa.pop('idade')
print(pessoa)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# atualiza a lista
pessoa.update({'idade': 40, 'Sexo': 'M'})
print(pessoa)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# erxclui a chave
del pessoa['cursos']
print(pessoa)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# apaga a lista
pessoa.clear()
print(pessoa)