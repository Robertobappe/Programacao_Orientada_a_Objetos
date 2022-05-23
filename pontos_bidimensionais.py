'''
PONTOS BIDIMENSIONAIS
Na célula abaixo, escreva o código de uma classe para representar um ponto em um espaço bidimensional, e uma função que recebe dois desses pontos e calcula a distância
entre eles:'''

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self):
    return ((self.x)**2 + (self.y)**2)**(1/2)   
