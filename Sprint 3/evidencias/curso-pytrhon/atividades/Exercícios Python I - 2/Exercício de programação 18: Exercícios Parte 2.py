def valores_unicos(dicionario):
    unico_valor = list(set(dicionario.values()))
    return unico_valor


speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

valor = valores_unicos(speed)
print(valor)