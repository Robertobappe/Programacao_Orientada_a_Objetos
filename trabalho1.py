#O primeiro trabalho consiste em resolver o problema 4 do Project Euler, cuja tradução segue:
#Um número palíndrome é o mesmo quando lido da esquerda para a direita ou da direita para a
#esquerda (descartando zeros à esquerda). A maior palíndrome constituída pelo produto de dois
#número de dois dígitos é 9009 = 91 × 99.

#Escreva um código para encontrar a maior palíndrome que é um produto de dois números de 3 dígitos.

#Você deve escrever o código em Python num arquivo com extensão .py, a ser executado diretamente pelo
#interpretador. O código deve imprimir o valor da palíndrome solicitada, sem esperar nenhuma
#interação do usuário.

#Precisa ser entregue apenas o arquivo com o código.

def prod_number(dig):
  L = []
  for i in range(999,101,-1):
    for j in range(999,101,-1):
      c = i*j
      if is_pal(c):
        L.append(c)
  return max(L)
  

def is_pal(number):   
  number = str(number)
  copy = number[::-1]

  if number == copy:
    return True
    
print(prod_number(3))
