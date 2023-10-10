class LanchoneteCaixa:  #iniciando os atributos fila e valor
    def __init__(self):
        self.sequencia_fila = []
        self.valor_total = 0.0

    def cliente_novo(self):
      if len(self.sequencia_fila) == 0:
        return None

      proximo_cliente_fila = self.sequencia_fila.pop(0)
      self.valor_total += proximo_cliente_fila.pagamento
      return proximo_cliente_fila
      

  
    def adicionar_cliente(self, consumidor): #método parainserir o cliente entrou na fila
        self.sequencia_fila.append(consumidor)

    def transferir_fila(self, outro_caixa):
      if len(self.sequencia_fila) == 0 and len(outro_caixa.sequencia_fila) > 0:
        tamanho_fila_outro = len(outro_caixa.sequencia_fila)
        metade_fila_outro = tamanho_fila_outro // 2

        for x in range(metade_fila_outro):
            cliente = outro_caixa.sequencia_fila.pop()
            self.sequencia_fila.insert(0, cliente)

#criando os caixas
primeiro_caixa = LanchoneteCaixa() #caixa1
segundo_caixa = LanchoneteCaixa() #caixa2


class LanchoneteCliente: #classe para representar os clientes da lanchonete
    def __init__(self, nome, pagamento):
        self.nome = nome
        self.pagamento = pagamento

#processando os comandos
while True: #laço while true para processar as decisoes até que o comando "FIM" seja recebido
    decisao = input().split() #recebendo decisao do usuario

    #se o comando for "entrou"
    if decisao[0] == "ENTROU:":

        #um novo cliente é adicionado à fila do e uma mensagem informando o nome do cliente e o número da fila é impressa
        nome = decisao[1]
        numeracao_caixa = int(decisao[2])
        pagamento = float(decisao[3])

        cliente = LanchoneteCliente(nome, pagamento)

        if numeracao_caixa == 1:
            primeiro_caixa.adicionar_cliente(cliente)
            segundo_caixa.transferir_fila(primeiro_caixa)
        elif numeracao_caixa == 2:
            segundo_caixa.adicionar_cliente(cliente)
            primeiro_caixa.transferir_fila(segundo_caixa)

        print(f"{nome} entrou na fila {numeracao_caixa}")

    #se o comando for 'proximo'
    elif decisao[0] == "PROXIMO:":
        numeracao_caixa = int(decisao[1])

        #o próximo cliente da fila do caixaé chamado e uma mensagem informando o nome do cliente e o número do caixa é impressa
        if numeracao_caixa == 1:
            chamar_cliente = primeiro_caixa.cliente_novo()
            segundo_caixa.transferir_fila(primeiro_caixa)
        elif numeracao_caixa == 2:
            chamar_cliente = segundo_caixa.cliente_novo()
            primeiro_caixa.transferir_fila(segundo_caixa)

        if chamar_cliente is not None:
            print(f"{chamar_cliente.nome} foi chamado para o caixa {numeracao_caixa}")

    elif decisao[0] == "FIM": #se o comando for "FIM" o loop while é interrompido
        break

#implementando o resultado do caixa 1
total_caixa1 = format(primeiro_caixa.valor_total, ".2f")

#implementando o resultado do caixa 2
total_caixa2 = format(segundo_caixa.valor_total, ".2f")

#outputmostrando o total
print(f"Caixa 1: R$ {total_caixa1}, Caixa 2: R$ {total_caixa2}")
