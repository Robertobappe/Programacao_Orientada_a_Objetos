'''1.Escreva uma função distancia que recebe dois Points como parâmetros e retorna a distância euclidiana entre eles.'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
        
def distance(point1, point2):
    X = point1.getX() - point2.getX() 
    Y = point1.getY() - point2.getY()
    return ((X**2)+(Y**2))**(1/2)

'''2.Crie um método reflect_x na classe Point que retorna um novo Point, que é a reflexão do ponto no eixo x. Por exemplo, Point(3, 5).reflect_x() é (3, -5)'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def reflect_x(self):
        self.y = -self.y
        return (self.x, self.y)

'''3.Crie um método slope_from_origin que retorna a inclinação da linha que liga o ponto à origem. Por exemplo,
>>> Point(4, 10).slope_from_origin()
2.5'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y    
    
    def slope_from_origin(self):
        return self.y / self.x

'''4.A equação de uma reta é “y = ax + b”, (ou talvez “y = mx + c”). Os coeficientes a e b são suficientes para descrever a linha. Escreva um método na classe Point que recebe outra
instância de Point e calcula a equação da reta que liga os dois pontos. O método deve retornar os dois coeficientes na forma de um tuple com dois valores. Por exemplo,
>>> print(Point(4, 11).get_line_to(Point(6, 15)))
>>> (2, 3)'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y       
    
    def get_line(self, x_, y_):
        self.x_ = x_
        self.y_ = y_
        
        a = (self.y - self.y_)/(self.x - self.x_)        
        y_ = a*(-self.x) + self.y
        
        return (a, y_)

