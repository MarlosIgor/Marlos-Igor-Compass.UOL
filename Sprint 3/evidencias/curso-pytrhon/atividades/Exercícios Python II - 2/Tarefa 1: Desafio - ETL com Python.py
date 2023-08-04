def separar_linha(linha):
    campos = []
    campo = ''
    entre_aspas = False
    for caractere in linha:
        if caractere == '"':
            entre_aspas = not entre_aspas
        elif caractere == ',' and not entre_aspas:
            campos.append(campo)
            campo = ''
        else:
            campo += caractere
    campos.append(campo)
    return campos


with open('actors.csv', 'r') as f:
    linhas = f.readlines()

registros = [separar_linha(linha.strip()) for linha in linhas]

cabecalho, dados = registros[0], registros[1:]


for registro in dados:
    registro[1] = float(registro[1])
    registro[2] = int(registro[2])
    registro[3] = float(registro[3])
    registro[5] = float(registro[5])


contador_mais_filmes = 0
ator_mais_filmes = ''
for registro in dados:
    if registro[2] > contador_mais_filmes:
        contador_mais_filmes = registro[2]
        ator_mais_filmes = registro[0]
with open('etapa-1.txt', 'w') as f:
    f.write(f'{ator_mais_filmes} tem o maior número de filmes, com {contador_mais_filmes} filmes.\n')


with open('etapa-2.txt', 'w') as f:
    f.write('Média de faturamento bruto por ator:\n')
    for registro in dados:
        ator = registro[0]
        media = registro[3]
        f.write(f'{ator}: {media:.2f}\n')


maior_media_arrecadacao_por_filme = 0
ator_maior_media_arrecadacao = ''
for registro in dados:
    if registro[3] > maior_media_arrecadacao_por_filme:
        maior_media_arrecadacao_por_filme = registro[3]
        ator_maior_media_arrecadacao = registro[0]
with open('etapa-3.txt', 'w') as f:
    f.write(f'{ator_maior_media_arrecadacao} tem a maior média de arrecadação por filme, com ${maior_media_arrecadacao_por_filme:.2f} milhões.\n')


contagem_filmes = {}
for registro in dados:
    filme = registro[4]
    if filme not in contagem_filmes:
        contagem_filmes[filme] = 0
    contagem_filmes[filme] += 1

filme_mais_frequente = ''
frequencia_filme_mais_frequente = 0
for filme, frequencia in contagem_filmes.items():
    if frequencia > frequencia_filme_mais_frequente:
        filme_mais_frequente = filme
        frequencia_filme_mais_frequente = frequencia

with open('etapa-4.txt', 'w') as f:
    f.write(f'O filme mais frequente em primeiro lugar é {filme_mais_frequente} com uma frequência de {frequencia_filme_mais_frequente}.\n')


atores_ordenados = []
for registro in dados:
    atores_ordenados.append((registro[0], registro[1]))
atores_ordenados.sort(key=lambda x: x[1], reverse=True)

with open('etapa-5.txt', 'w') as f:
    for ator, arrecadacao in atores_ordenados:
        f.write(f'{ator}: ${arrecadacao:.2f} milhões\n')
