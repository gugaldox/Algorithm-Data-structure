def subset_recursivo(lista, caminho, subset, index):
    if subset:
      caminho.append(subset[:])

    for i in range(index, len(lista)):
        subset.append(lista[i])
        subset_recursivo(lista, caminho, subset, i + 1)
        subset.pop()  #backtraking é isso aqui


def subsets(lista):
    subset = []
    caminhos = [[]]
    index = 0
    if lista != [' ']:
      subset_recursivo(lista, caminhos, subset, index)
    return caminhos


planetas = input().split(', ')
planetas.sort()
rotas = subsets(planetas)

print(f'O número de subsets de visitação é {len(rotas)}')
print(f'São eles: {rotas}')