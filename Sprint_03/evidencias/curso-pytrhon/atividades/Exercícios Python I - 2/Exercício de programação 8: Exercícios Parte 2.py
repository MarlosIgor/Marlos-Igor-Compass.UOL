def palindromo(palavra):
    return palavra == palavra[::-1]


palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in palavras:
    if palindromo(palavra):
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")
