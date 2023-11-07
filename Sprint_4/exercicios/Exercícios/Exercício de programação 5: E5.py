import csv

with open('estudantes.csv', 'r') as f:
    reader = csv.reader(f)
    estudantes = []
    for i in reader:
        nome = i[0]
        grades = i[1:]
        grades = list(map(int, grades))
        estudantes.append((nome, grades))

    estudantes.sort(key=lambda x: x[0])

    for estudante in estudantes:
        nome = estudante[0]
        grades = estudante[1]
        tres_maiores_notas = sorted(grades, reverse=True)[:3]
        average = round(sum(tres_maiores_notas) / len(tres_maiores_notas), 2)
        print(f'Nome: {nome} Notas: {tres_maiores_notas} Média: {average}')
