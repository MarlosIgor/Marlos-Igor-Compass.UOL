# pecorrendo uma string
palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=',')
print('Fim')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# pecorrendo uma lista
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)
print('-=-=-=-=-=-=-=-=-')

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

# pecorrendo uma tupla
dias_semana = ('Domingo', 'Segunda', 'Terca',
               'Quarta', 'Quinta', 'Sexta', 'Sabado')
for dia in dias_semana:
    print(f'Hoje e {dia}')