#entrada inicial para receber as duas listas do usuario#
filmes_lista1 = input().split(',') #lista 1#
filmes_lista2 = input().split(',') #lista2#

#CLASSE REPRESENTADOS
class FilmesCinema:
    def __init__(self, filmes_cinema):
        self.filmes_cinema = filmes_cinema  #inicializa a lista de filmes#

#FUNÇÃO PARA ENCONTARR O FILME DA MEDIANA#     
    def achando_filme(self):
        filmes_listados = self.ordenacao_mergesort(self.filmes_cinema)
        quant_filmes_listados = len(filmes_listados)
        indice_mediana = quant_filmes_listados // 2
        filme_do_meio = filmes_listados[indice_mediana]
        return filme_do_meio


#FUNÇÃO PARA REPRESENTAR O ALGORITMO DE ORDENAÇÃO MAERGESORT#
    def ordenacao_mergesort(self, lista_filmes):
        if len(lista_filmes) <= 1:
            return lista_filmes  #caso base da recursiva: lista de tamanho 1 ou vazia já está ordenada pq não tem muitos filmes#

        ponto_medio = len(lista_filmes) // 2  #encontrando o ponto médio da lista#

        #divide a lista em duas metades#
        primeira_metade = lista_filmes[:ponto_medio]  #metade esquerda#
        segunda_metade = lista_filmes[ponto_medio:] #metade direita#

        #chamando recursiva para ordenar as duas metades#
        primeira_metade = self.ordenacao_mergesort(primeira_metade)
        segunda_metade = self.ordenacao_mergesort(segunda_metade)

        #realizabdo a mescla ordenada das duas metades#
        return self.combinando_listas(primeira_metade, segunda_metade)
    
#FUNÇÃO PARA MESCLAR AS LISTAS ORDENADS#
    def combinando_listas(self, esquerda, direita):
        x = y = 0  # indices para percorrer as listas esquerda e direita#
        combinacao_lista = []  #lista para armazenar o processo de combinar duas listas ordenadas#

        #percorre as listas esquerda e direita e compara os elementos para combinar/mesclar#
        while x < len(esquerda) and y < len(direita):
            if esquerda[x] < direita[y]:
                combinacao_lista.append(esquerda[x])
                x += 1
            else:
                combinacao_lista.append(direita[y])
                y += 1

        #adiciona os elementos restantes, caso alguma das listas ainda tenha elementos#
        combinacao_lista.extend(esquerda[x:])
        combinacao_lista.extend(direita[y:])
        return combinacao_lista



#cri# criação do objeto lista_filmes com as duas listas de filmes
lista_filmes = FilmesCinema(filmes_lista1 + filmes_lista2)

# encontrar o filme da mediana e passá-lo para a variável
filme_mediana = lista_filmes.achando_filme()

# encontrar o índice do filme na lista ordenada
mediana_indice = lista_filmes.ordenacao_mergesort(lista_filmes.filmes_cinema).index(filme_mediana) + 1

# output
print(f'Os amigos decidiram assistir a {filme_mediana} que estava na posição {mediana_indice} da lista.')
