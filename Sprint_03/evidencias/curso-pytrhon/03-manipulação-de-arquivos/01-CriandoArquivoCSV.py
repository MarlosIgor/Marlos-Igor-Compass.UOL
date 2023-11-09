# arquivo
arquivo = open('pessoas.csv')
# adicionando os dados do arquivo em uma variavel
dados = arquivo.read()
# fechando o arquivo com os dados salvo na variavel
arquivo.close()

for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))