produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

# retorna a CHAVE
for chave in produto:
    print(chave)
print('-=-=-=-=-=-=-=-=-')

# retorna o VALOR
for valor in produto.values():
    print(valor)
print('-=-=-=-=-=-=-=-=-')

# retorna CHAVE e VALOR
for chave, valor in produto.items():
    print(chave, '=', valor)