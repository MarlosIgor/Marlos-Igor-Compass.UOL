import json

with open('person.json') as arquivo:
    person = json.load(arquivo)
print(person)