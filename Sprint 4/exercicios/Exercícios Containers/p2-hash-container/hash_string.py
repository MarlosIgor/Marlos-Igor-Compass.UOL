import hashlib

n = 1
print("Digite uma string para gerar o hash ou 'sair' para encerrar o programa.\n")
while True:
    input_string = input(f"{n}-Digite: ")

    if input_string.lower() == "sair":
        print('Volte sempe!!!')
        break

    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()
    print(f"Hash SHA-1 da string: {sha1_hash}\n")
    n += 1
