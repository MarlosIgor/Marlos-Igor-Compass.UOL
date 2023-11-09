animais = ['gato', 'cachorro', 'elefante', 'leão', 'tigre', 'girafa', 'zebra', 'hipopótamo', 'rinoceronte', 'macaco',
           'gorila', 'panda', 'urso', 'lobo', 'raposa', 'coelho', 'tartaruga', 'crocodilo', 'pinguim', 'golfinho']

animais.sort()

for animal in animais:
    print(animal)

with open('animais.csv', 'w') as f:
    for animal in animais:
        f.write("%s\n" % animal)
