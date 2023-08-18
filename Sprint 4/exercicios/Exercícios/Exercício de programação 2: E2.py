def conta_vogais(texto: str) -> int:
    vogais = set("aeiou")

    return len(list(filter(lambda letra: letra in vogais, texto.lower())))