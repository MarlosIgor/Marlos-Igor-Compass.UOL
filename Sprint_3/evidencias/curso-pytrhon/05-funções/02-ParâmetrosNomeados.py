def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    # teste 1
    print(tag_bloco('bloco'))
    # teste 2
    print(tag_bloco('inline e classe', 'info', True))
    # teste 3
    print(tag_bloco('inline', inline=True))
    # teste 4
    print(tag_bloco('falhou', 'error'))