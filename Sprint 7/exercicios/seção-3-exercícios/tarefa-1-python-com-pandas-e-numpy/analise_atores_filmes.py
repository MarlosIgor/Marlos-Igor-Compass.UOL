import pandas as pd

df = pd.read_csv('actors.csv')

ator_com_mais_filmes = df[df['Number of Movies'] == df['Number of Movies'].max()]
nome_ator_com_mais_filmes = ator_com_mais_filmes.iloc[0]['Actor']
numero_de_filmes = ator_com_mais_filmes.iloc[0]['Number of Movies']

média_numero_de_filmes = df['Number of Movies'].mean()

ator_com_maior_média_por_filme = df[df['Average per Movie'] == df['Average per Movie'].max()]
nome_ator_com_maior_média_por_filme = ator_com_maior_média_por_filme.iloc[0]['Actor']

filmes_mais_frequentes = df['#1 Movie'].value_counts().head(1)
nome_filme_mais_frequente = filmes_mais_frequentes.index[0]
frequência_filme_mais_frequente = filmes_mais_frequentes.iloc[0]

print("1. Ator/atriz com o maior número de filmes:", nome_ator_com_mais_filmes, "com", numero_de_filmes, "filmes")

print("2. Média da coluna de número de filmes:", média_numero_de_filmes)

print("3. Ator/atriz com a maior média por filme:", nome_ator_com_maior_média_por_filme)

print("4. Filme(s) mais frequente(s):", nome_filme_mais_frequente, "com", frequência_filme_mais_frequente, "ocorrências")


