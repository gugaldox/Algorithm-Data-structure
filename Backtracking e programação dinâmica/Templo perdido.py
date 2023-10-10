def maximo(salas, colares_sala):
    if salas == 0:
        return 0
    elif salas == 1:
        return colares_sala[0]

    soma = salas*[0]
    soma[0] = colares_sala[0]
    soma[1] = max(colares_sala[1], colares_sala[0])

    for i in range(2, salas):
        soma[i] = max(colares_sala[i]+soma[i-2], soma[i-1])

    return soma[-1]  #maior numeor


numero = int(input())
colares = input().split()
colares = [int(colar) for colar in colares]

max_colares = maximo(numero, colares)
print(f'{max_colares} colares podem ser retirados.')
