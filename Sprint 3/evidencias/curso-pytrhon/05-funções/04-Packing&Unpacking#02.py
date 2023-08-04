def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    # teste 1
    print(tag_bloco('inline e classe', 'info', True))
    # teste 2
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
