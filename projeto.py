from ast import Break
from fila import *


# Classe que direciona a sua devida função de tratativa

class operacao:
    def __init__(self) -> None:
        self.a = FilaArray()

    #  Armazena a compra na fila   

    def compra(self, quantidade, valor):
        self.a.armazenar(quantidade=quantidade, valor=valor)

    # Insere a venda e quantidade e retorna o saldo    

    def venda(self, quantidade, valor):
        print(self.a.venda(quanti=quantidade, val=(valor)))

    # Retorna a ação anterior

    def apagar_acao(self):
        print(self.a.desfazer())

# Função inicial para o input das ações

def projeto():
    f = operacao()
    while True:
        # exemplo de input "c,10,20" ; "v,10,10" ; "<"
        entrada = input("tipo de entrada => C, quantidade, valor para compra; V, quantidade, valor para venda; '<' voltar a ultima operação: ")
        if entrada == "<":
            print(f"{f.apagar_acao()}")

        elif entrada[0].lower() == "c" or entrada[0].lower() == "v":
            acao, quantidade, valor = entrada.split(",")
            if acao.lower() == "c":
                print(f.compra(quantidade= int(quantidade), valor=int(valor)))

            elif acao.lower() == "v":
                print(f.venda(quantidade= int(quantidade), valor=int(valor)))

        else: print("Operação inválida"); Break