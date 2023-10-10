#definindo a função "fogueira" que conta quantas fogueiras são puladas e se o personagem conseguiu pular todas
def fogueira(lista_cont):
    fogueiras = 0
    resultado = False

    while True:
        indice_inicial = 0
        inicio_cod = lista_cont[indice_inicial]
        try:
            try:
                #verificandose há apenas um elemento na lista, o que significa que todas as fogueiras foram puladas
                if len(lista_cont) == 1:
                    resultado = True
                    break
                # veerificando se o próximo item a ser acessado é igual a zero, o que indica que não há fogueiras restantes
                elif quantidade_fog == 0:
                    resultado = False
                    break
            except:
                1 + 1

            while indice_inicial <= int(inicio_cod):
                quantidade_fog = lista_cont[indice_inicial]
                indice_inicial += 1

            fogueiras += 1

            quantidade_fog = int(quantidade_fog)

            indice_inicial -= 1
            lista_cont = lista_cont[indice_inicial:]

        except:
            resultado = True
            fogueiras += 1 #somando a fogueira
            break

    return fogueiras, resultado


#função para rodara entrada e retornar uma lista de números
def retornar_lista(qunt, input_inicial):
    nome, *numeros_pulos = input_inicial.split(" ")
    lista_numeros = numeros_pulos
    return lista_numeros

#recebendo entrada para gabriel (o primeiro da fila)
lista_numero_digitado = int(input())
output_usuario = input()
gab = retornar_lista(lista_numero_digitado, output_usuario)
quantidade_fogueiras, resultado = fogueira(gab)
if resultado:
    print('Gabriel conseguiu!')
    print(f'Gabriel precisou pular {quantidade_fogueiras} fogueiras')
else:
    print('Ah, que pena, Gabriel não conseguiu!')

#recebendo entrada e rodando para joao (o segundo da ordem)
lista_numero_digitado = int(input())
output_usuario = input()
jao = retornar_lista(lista_numero_digitado, output_usuario)
quantidade_fogueiras, resultado = fogueira(jao)
if resultado:
    print('João conseguiu!')
    print(f'João precisou pular {quantidade_fogueiras} fogueiras')
else:
    print('Ah, que pena, João não conseguiu!')

#função para rodara entrada e retornar uma lista de números
def retorno_lista(qunt, input_inicial):
    nome, *numeros_pulos = input_inicial.split(" ")
    lista_numeros = numeros_pulos
    return lista_numeros

#recebendo entrada e rodadando para edu (o penultimo da ordem)
lista_numero_digitado = int(input())
output_usuario = input()
eduardo = retorno_lista(lista_numero_digitado, output_usuario)
quantidade_fogueiras, resultado = fogueira(eduardo)
if resultado:
    print('Edu conseguiu!')
    print(f'Edu precisou pular {quantidade_fogueiras} fogueiras')
else:
    print('Ah, que pena, Edu não conseguiu!')

#recebendo entrada e rodando para carlos (o ultimo da ordem)
lista_numero_digitado = int(input())
output_usuario = input()
carlos = retorno_lista(lista_numero_digitado, output_usuario)
quantidade_fogueiras, resultado = fogueira(carlos)
if resultado:
    print('Carlos conseguiu!')
    print(f'Carlos precisou pular {quantidade_fogueiras} fogueiras')
else:
    print('Ah, que pena, Carlos não conseguiu!')