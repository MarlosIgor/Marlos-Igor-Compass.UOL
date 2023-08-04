# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def finonacci(quantidade, sequencia=(0, 1)):
    if len(sequencia) == quantidade:
        return sequencia
    return finonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    for fib in finonacci(20):
        print(fib)
