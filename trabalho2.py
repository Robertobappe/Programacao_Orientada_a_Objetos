'''Segundo Trabalho de Programação Orientada a Objetos
Descrição

Você precisa implementar o código de uma classe denominada MovingStats que fornece algumas estatísticas móveis sobre uma sequência de valores.
Isso significa que vão sendo fornecidos continuamente novos valores, e a qualquer momento o usuário pode requisitar as estatísticas correntes,
considerando todos os valores já fornecidos. Depois ele pode ir fornecendo novos valores e as estatísticas vão sendo atualizadas.

Aqui vamos nos importar apenas com quatro estatisticas: o número de valores já fornecidos, o menor valor, o maior valor e a média dos valores.

O uso da classe será da seguinte forma (veja também o código de teste abaixo):

st = MovingStats()
print(st.current_size()) # imprime 0
print(st.current_min())  # imprime None
print(st.current_max())  # imprime None
print(st.current_mean()) # imprime None

for i in range(-2, 11):
    st.insert(i)
print(st.current_size()) # imprime 13
print(st.current_min())  # imprime -2
print(st.current_max())  # imprime 10
print(st.current_mean()) # imprime 4

st.insert(-10)
st.insert(3)
print(st.current_size()) # imprime 15
print(st.current_min())  # imprime -10
print(st.current_max())  # imprime 10
print(st.current_mean()) # imprime 3

Um limitação ä implementação é que se espera que será fornecido um número muito grande de valores. Isto significa que não é permitido armazenar
todos os valores para calcular as estatísticas quando necessário. Você precisa guardar apenas os dados necessários para a atualização das estatísticas
sempre que um novo valor for fornecido.

Nota: Em geral, estatísticas móveis não calculam usando todos os valores fornecidos, mas apenas os N últimos, onde N é o tamanho de uma janela de interesse.
O que estou pedindo aqui é diferente, e usa todos os valores. É também mais fácil de implementar.
Implementação

Coloque o seu código de implementação na célula abaixo:'''

import numpy as np

class MovingStats:
    def __init__(self):
        self.size = 0
        self.min = None
        self.max = None
        self.mean = None
        self.L = []
        
    def current_size(self):
        return self.size
    
    def current_min(self):
        return self.min
    
    def current_max(self):
        return self.max
    
    def current_mean(self):
        return self.mean
    
    def insert(self, value):
        self.L.append(value)
        self.size = len(self.L)
        self.min = min(self.L)
        self.max = max(self.L)
        self.mean = np.mean(self.L)
        

'''Testes
Teste de inicialização'''

st = MovingStats()
assert st.current_size() == 0, 'Valor inicial errado para tamanho corrente'
assert st.current_min() is None, 'Valor inicial errado para mínimo corrente'
assert st.current_max() is None, 'Valor inicial errado para máximo corrente'
assert st.current_mean() is None, 'Valor inicial errado para média corrente'
print('Inicialização correta')

'''Teste de primeiro valor'''

st = MovingStats()
st.insert(2)
assert st.current_size() == 1, 'Erro para tamanho corrente com uma inserção'
assert st.current_min() == 2, 'Valor para mínimo corrente errado com uma inserção'
assert st.current_max() == 2, 'Valor para máxmo corrente errado com uma inserção'
assert st.current_mean() == 2, 'Valor para médio corrente errado com uma inserção'
print('Inserção de apenas um valor positivo funcionou')

st = MovingStats()
st.insert(-5)
assert st.current_size() == 1, 'Erro para tamanho corrente com uma inserção'
assert st.current_min() == -5, 'Valor para mínimo corrente errado com uma inserção'
assert st.current_max() == -5, 'Valor para máxmo corrente errado com uma inserção'
assert st.current_mean() == -5, 'Valor para médio corrente errado com uma inserção'
print('Inserção de apenas um valor negativo funcionou')

'''Teste aleatório'''

import random

N = 10_000
values = [random.randint(-10000, 10000) for _ in range(N)]
st = MovingStats()
for i in range(N):
    st.insert(values[i])
    assert st.current_size() == i + 1, 'Tamanho errado'
    assert st.current_min() == min(values[:i+1]), 'Mínimo errado'
    assert st.current_max() == max(values[:i+1]), 'Máximo errado'
    assert st.current_mean() == sum(values[:i+1]) / (i + 1), 'Média errada'
print('Tudo certo!')





















        
