from logging import exception
from deck import *

# -------------------------- FILA ARRAY ----------------------

class FilaVazia(Exception):
  pass

class FilaArray:
  CAPACIDADE_PADRAO = 5 

  def __init__(self):
    self.acao = deck()
    self.saldo_anterior = deck()
    self._dados = [None] * FilaArray.CAPACIDADE_PADRAO
    self._tamanho = 0
    self._inicio = 0
    self.saldo = 0

  def __len__(self):
    return self._tamanho

  def is_empty(self):
    return self._tamanho == 0

  def first(self):
    if self.is_empty():
      raise FilaVazia('A Fila está vazia')
    return self._dados[self._inicio]

  def dequeue(self):
    if self.is_empty():
      raise FilaVazia('A Fila está vazia')
    result = self._dados[self._inicio]
    self._dados[self._inicio] = None
    self._inicio = (self._inicio + 1) % len(self._dados)
    self._tamanho -= 1
    return result

  def enqueue(self, e): # - - x x x - 
    if self._tamanho == len(self._dados):
      self._altera_tamanho(2 * len(self._dados))
    disponivel = (self._inicio + self._tamanho) % len(self._dados)
    self._dados[disponivel] = e
    self._tamanho += 1

  def _altera_tamanho(self, novo_tamanho):   
    dados_antigos = self._dados              
    self._dados = [None] * novo_tamanho     
    posicao = self._inicio
    for k in range(self._tamanho):          
      self._dados[k] = dados_antigos[posicao] 
      posicao = (1 + posicao) % len(dados_antigos) 
    self._inicio = 0                        

  def show(self):
    print(self)

  def __str__(self):
    posicao = self._inicio
    result = "["
    for k in range(self._tamanho):
      result += str(self._dados[posicao]) + ", "
      posicao = (1 + posicao) % len(self._dados)
    result += f'] tamanho: {len(self)} capacidade {len(self._dados)}\n'
    return result

# -------------PROGRAMA-----------------

          # Cadastrar Compra
  def armazenar(self, valor,quantidade):
    self.acao.push_right(self._dados)
    self.saldo_anterior.push_right(self.saldo)
    self.enqueue(f"{quantidade},{valor}")


          # Inserir Venda e fazer a comparação retornando o saldo e a diferença de valor em cada dia


  def venda(self,quanti,val):
    self.acao.push_right(self._dados)
    self.saldo_anterior.push_right(self.saldo)
    quant = quanti
    dia = 1
    while quant:
      qnt,va = self.dequeue().split(",")
      quantidade = int(qnt)
      valor = int(va)
      if quantidade < quant:
        a = -valor+val
        print(f"A diferença do valor (compra x venda) do dia {dia} é {a} Reais")
        self.saldo += a*quantidade
        dia += 1
        quant -= quantidade
      else:
        a = -valor+val
        print(f"A diferença do valor (compra x venda) do dia {dia} é {a} Reais")
        self.saldo += a*quant
        dia += 1
        a = quantidade - quant
        self.nova_fila(quantida=a, valo=valor)
        quant -= quant
    return f"saldo atual {self.saldo} Reais"

          # Desfazer a ultima ação

  def desfazer(self):
    try:
      self.dados = self.acao.pop_right()
      self.saldo = self.saldo_anterior.pop_right()
    except: print("Sem retornos!")
    return f"Saldo atual {self.saldo} Reais"


  # --------------- Refaz a fila se caso sobrar alguma compra que não foi vendida no dia --------------

  def nova_fila(self,quantida,valo):
    refazer = self._tamanho
    self.enqueue(f"{quantida},{valo}")
    while refazer:
      self.enqueue(self.dequeue())
      refazer -= 1